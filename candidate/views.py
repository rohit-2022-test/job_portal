from django.shortcuts import render, redirect
from account.models import UserDetail
from master_table.models import Location
from .models import (
    UserCourse,
    UserEducation,
    UserExperience,
    UserLanguage,
    UserProject,
    UserSkill
)
from .form import UserExperienceForm
# Create your views here.

def candidate_form(request):
    if 'languege' in request.path:
        return render(request,'candidate/forms/languege_form.html')
    
    if 'skill' in request.path:
        return render(request,'candidate/forms/skill_form.html')
    
    if 'project' in request.path:
        return render(request,'candidate/forms/project_form.html')
    
    if 'education' in request.path:
        if request.method == 'POST':
            institute_name = request.POST.get('institute_name')
            course = request.POST.get('course')
            grade = request.POST.get('grade')
            subject = request.POST.get('subject')
            start_data = request.POST.get('start_data')
            end_data = request.POST.get('end_data')
            activity = request.POST.get('activity')
            description = request.POST.get('description')

            UserEducation.objects.create(user_id=request.user,institute_name=institute_name,course=course,subject=subject,
                            grade=grade,activities=activity,start_date=start_data,end_date=end_data,description=description)
            return redirect('candidate_detail')

        return render(request,'candidate/forms/education_form.html')
    
    if 'experiance' in request.path:
        form = UserExperienceForm()
        if request.method == 'POST':
            city = request.POST.get('city')
            form = UserExperienceForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.location_id = Location.objects.get(city=city)
                obj.user_id = request.user
                obj.save()
                form.save()
                return redirect('candidate_detail')
        
        cities = Location.objects.all().values_list('city',flat=True)
        states = Location.objects.all().values_list('state',flat=True)
        context = {
            'form' : form,
            'cities' : cities,
            'states' : states
        }
        return render(request,'candidate/forms/experiance_form.html',context)
    
    if 'cource' in request.path:
        if request.method == 'POST':
            cource_name = request.POST.get('cource_name') 
            associate = request.POST.get('associate')
            start_data = request.POST.get('start_data')
            end_data = request.POST.get('end_data')
            description = request.POST.get('description')

            UserCourse.objects.create(user_id=request.user,course_name=cource_name,associate=associate,
                                      start_date=start_data,end_date=end_data,description=description)
            return redirect('candidate_detail')
        
        return render(request,'candidate/forms/cource_form.html')
    
    
def candidate_detail(request):
    
    candidate_detail = UserDetail.objects.filter(user_id=request.user)
    candidate_experience = UserExperience.objects.filter(user_id=request.user)
    candidate_education = UserEducation.objects.filter(user_id=request.user)
    candidate_project = UserProject.objects.filter(user_id=request.user)
    candidate_cource = UserCourse.objects.filter(user_id=request.user)
    candidate_language = UserLanguage.objects.filter(user_id=request.user)
    candidate_skill = UserSkill.objects.filter(user_id=request.user)

    skill_language = {'language':candidate_language,'skill':candidate_skill}
    education_experience = {'education':candidate_education,'experience':candidate_experience}
    project_cource = {'project':candidate_project,'cource':candidate_cource}

    context = {
        'candidatedetail' : candidate_detail,
        'project_cource' : project_cource,
        'skill_language' : skill_language,
        'education_experience' : education_experience
    }
    return render(request,'candidate/candidate_detail.html',context)
