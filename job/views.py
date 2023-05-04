from django.db.models import Count
from django.shortcuts import redirect, render
from job.filter import JobFilter
from job.models import Job, JobApplicants
from django.core.mail import send_mail
from django.core.paginator import Paginator


# Create your views here.
def job_list(request):
    job_list = Job.objects.all()

    job_type_dict = {}
    job_type_list = ['full-time',
                    'part-time',
                    'self-employed',
                    'frelance',
                    'contract',
                    'internship']
    for i in job_type_list:
        job_type_count = Job.objects.filter(job_type=i).count()
        job_type_dict[i] = job_type_count

    #Filter 
    filter_job = JobFilter(request.GET, queryset=job_list)

    paginator = Paginator(job_list,2)
    page = request.GET.get('page')
    paged_list = paginator.get_page(page)

    context = {
        'job_list' : job_list,
        'filter' : filter_job,
        'job_type_dict' : job_type_dict,
        'paged_list' : paged_list
    }
    return render(request,'job/job_list.html',context)

def job_filter(request):
    job_list = Job.objects.all()
    job_type_dict = {}
    job_type_list = ['full-time',
                    'part-time',
                    'self-employed',
                    'frelance',
                    'contract',
                    'internship']
    for i in job_type_list:
        job_type_count = Job.objects.filter(job_type=i).count()
        job_type_dict[i] = job_type_count

    #Filter 
    filter_job = JobFilter(request.GET, queryset=job_list)

    context = {
        'job_list' : job_list,
        'filter' : filter_job,
        'job_type_dict' : job_type_dict,
    }
    return render(request,'job/job_filter.html',context)


def job_detail(request,id): 
    job_detail = Job.objects.get(id=id)
    context = {
        'job_detail' : job_detail,
    }
    return render(request,'job/job_detail.html',context)

def job_apply(request):
    if request.method == 'POST':
        job_id = request.POST.get('id')
        job_instance_id = Job.objects.get(id=job_id)
        if job_instance_id.applicants_collection_mode == 'email':    
            JobApplicants.objects.create(candidate_id=request.user,job_id=job_instance_id)
            send_mail(
                'Inquiry for Job',
                f"There has been an inquiry for job aaplication. Name: {request.user}",
                'joshijaya.shivinfotech@gmail.com',
                ('joshijaya29@gmail.com',job_instance_id.applicants_collection_link_email,),
                fail_silently=False
                ) 

            return redirect('job_list')
        else: 
            JobApplicants.objects.create(candidate_id=request.user,job_id=job_instance_id)

            return redirect(job_instance_id.applicants_collection_link_email)
  