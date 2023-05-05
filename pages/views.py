from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.db.models import Q
from pages.filter import JobFilter
from job.models import Job
from pages.form import ContactForm
from pages.models import Contact
from django.core.paginator import Paginator

def index(request):
    filter_job = JobFilter(request.GET, queryset=Job.objects.all())
    context = {
        'filter' : filter_job,
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about_us.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            usermessage = form.cleaned_data.get('message')
            name = form.cleaned_data.get('name')
            subject = form.cleaned_data.get('subject')
            email = form.cleaned_data.get('email')
            date_of_request = Contact.objects.filter(name=name).values_list('created_at',flat=True).last()
            send_mail_dict = {'joshijaya29@gmail.com':f"There has been an inquiry for {subject}. Name: {name} ,Message: {usermessage}. Date: {date_of_request}.", email:f"There has been an inquiry for {subject}.Message: {usermessage}."}
            for send_data in send_mail_dict:
                send_mail(
                    'Job Inquiry',
                    send_mail_dict[send_data],
                    'joshijaya.shivinfotech@gmail.com',
                    (send_data,),
                    fail_silently=False
                    )
            return redirect('index')
        else:
            return redirect('contact')
    
    context = {
        'form' : form
        }
    return render(request,'pages/contact.html',context)


def search(request):
    job_filter = Job.objects.all()
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            job_filter = job_filter.filter(Q(job_title__icontains=keywords) | Q(job_type__icontains=keywords) | Q(datails__icontains=keywords) | Q(workplace_type__icontains=keywords))


    filter_job = JobFilter(request.GET, queryset=job_filter)
    paginator = Paginator(filter_job.qs,2)
    page = request.GET.get('page')
    paged_list = paginator.get_page(page)
    context = {
        'paged_list' : job_filter,
        'paged_list' : paged_list,

    }
    return render(request,'pages/search.html',context)
