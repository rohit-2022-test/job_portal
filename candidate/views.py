from django.shortcuts import render
from django.contrib.auth.models import User
from account.models import UserDetail
from .models import UserCourse,UserEducation,UserExperience,UserLanguage,UserProject,UserSkill
# Create your views here.

def candidate_form(request):
    if 'languege' in request.path:
        return render(request,'candidate/forms/languege_form.html')
    if 'project' in request.path:
        return render(request,'candidate/forms/project_form.html')
    if 'education' in request.path:
        return render(request,'candidate/forms/education_form.html')
    if 'experiance' in request.path:
        return render(request,'candidate/forms/experiance_form.html')
    if 'cource' in request.path:
        return render(request,'candidate/forms/cource_form.html')
    
    
def candidate_detail(request,id):
    
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