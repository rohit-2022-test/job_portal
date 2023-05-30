from django.shortcuts import render, redirect
from django.core.mail import send_mail
from pages.form import ContactForm
from pages.models import Contact

def index(request):
    return render(request,'pages/index.html')

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

