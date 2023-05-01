from django.shortcuts import render, redirect
from account.models import UserDetail
from django.db.models import Prefetch
from django.contrib.auth.models import User
from django.contrib import messages
from master_table.models import Language, Location, Skill
from .models import (
    UserCourse,
    UserEducation,
    UserExperience,
    UserLanguage,
    UserProject,
    UserSkill
)
from .form import (
    UserDetailForm,
    UserExperienceForm,
    UserProjectForm,
)
# Create your views here.

def candidate_create_form(request):

    if 'candidate_detail' in request.path:
        try:
            form = UserDetailForm()
            if request.method == 'POST':
                city = request.POST.get('city')
                form = UserDetailForm(request.POST, request.FILES)
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.location_id = Location.objects.get(city=city)
                    obj.user_id = request.user
                    obj.save()
                    form.save()
                    return redirect('candidate_detail')
                
        except Exception:
            messages.success(request,'Your detail is already exists.')
            return redirect('candidate_detail')
            
        cities = Location.objects.all().values_list('city',flat=True)
        states = Location.objects.all().values_list('state',flat=True)
        context = {
            'form' : form,
            'cities' : cities,
            'states' : states
        }
        return render(request,'candidate/forms/candidate_form.html',context)

    if 'language' in request.path:

        if request.method == 'POST':
            language_name = request.POST.get('language_name')
            proficiency = request.POST.get('proficiency')

            language = Language.objects.all()
            if language_name not in language:
                language = Language.objects.create(name=language_name)
            else:
                language = Language.objects.get(name=language_name)
            
            UserLanguage.objects.create(user_id=request.user,language_id=language,proficiency=proficiency)
    
            return redirect('candidate_detail')
        
        languages = Language.objects.all().values_list('name',flat=True)
        context = {
            'languages' : languages
        }
            
        return render(request,'candidate/forms/languege_form.html',context)
    
    if 'skill' in request.path:
        if request.method == 'POST':
            skill_name = request.POST.get('skill_name')
 
            skill = Skill.objects.all()
            if skill_name not in skill:
                skill = Skill.objects.create(name=skill_name)
            else:
                skill = Skill.objects.get(name=skill_name)

            UserSkill.objects.create(user_id=request.user,skill_id=skill) 

            return redirect('candidate_detail')
        
        skilles = Skill.objects.all().values_list('name',flat=True)
        context = {
            'skilles' : skilles
        }
        
        return render(request,'candidate/forms/skill_form.html',context)
    
    if 'project' in request.path:
        form = UserProjectForm()
        if request.method == 'POST':
            form = UserProjectForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user_id = request.user
                obj.save()
                form.save()
                return redirect('candidate_detail')
            
        context = {
            'form' : form,
        }
        return render(request,'candidate/forms/project_form.html',context)
    
    if 'education' in request.path:
        if request.method == 'POST':
            institute_name = request.POST.get('institute_name')
            course = request.POST.get('course')
            grade = request.POST.get('grade')
            subject = request.POST.get('subject')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            activity = request.POST.get('activity')
            description = request.POST.get('description')

            if start_date == '':
                start_date = False
            else:
                start_date = start_date

            if end_date == '':
                end_date = False
            else:
                end_date = end_date

            UserEducation.objects.create(user_id=request.user,institute_name=institute_name,course=course,subject=subject,
                            grade=grade,activities=activity,start_date=start_date,end_date=end_date,description=description)
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
            currently_working = bool(request.POST.get('currently_working'))
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            description = request.POST.get('description')

            if start_date == '':
                start_date = False
            else:
                start_date = start_date

            if end_date == '':
                end_date = False
            else:
                end_date = end_date

            UserCourse.objects.create(user_id=request.user,course_name=cource_name,associate=associate,
                                      currently_working=currently_working,start_date=start_date,end_date=end_date,
                                      description=description)
            return redirect('candidate_detail')
        
        return render(request,'candidate/forms/cource_form.html')

def candidate_update_form(request,id):
    if 'update_education' in request.path:
        if request.method == 'POST':
            institute_name = request.POST.get('institute_name')
            course = request.POST.get('course')
            grade = request.POST.get('grade')
            subject = request.POST.get('subject')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            activity = request.POST.get('activity')
            description = request.POST.get('description')

            if start_date == '':
                start_date = False
            else:
                start_date = start_date

            if end_date == '':
                end_date = False
            else:
                end_date = end_date

            UserEducation.objects.filter(id=id).update(institute_name=institute_name,course=course,grade=grade,
                                                       subject=subject,start_date=start_date,end_date=end_date,
                                                       activities=activity,description=description)
            return redirect('candidate_detail')

        update_education = UserEducation.objects.filter(id=id)
        context = {
            'update_education' : update_education
        }
        return render(request,'candidate/update_form/education_form.html',context)

    if 'update_experience' in request.path:
        if request.method == 'POST':
            company_name = request.POST.get('company_name')
            job_title = request.POST.get('job_title')
            job_type = request.POST.get('job_type')
            city = request.POST.get('city')
            workplace_type = request.POST.get('workplace_type')
            currently_working = bool(request.POST.get('currently_working'))
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            description = request.POST.get('description')

            city_state = Location.objects.get(city=city)

            if start_date == '':
                start_date = False
            else:
                start_date = start_date

            if end_date == '':
                end_date = False
            else:
                end_date = end_date
            
            UserExperience.objects.filter(id=id).update(company_name=company_name,job_title=job_title,
                                                        job_type=job_type,location_id=city_state,
                                                        start_date=start_date,workplace_type=workplace_type,
                                                        currently_working=currently_working,description=description,
                                                        end_date=end_date)
            return redirect('candidate_detail')

        cities = Location.objects.all().values_list('city',flat=True)
        states = Location.objects.all().values_list('state',flat=True)
        update_experience = UserExperience.objects.filter(id=id)
        context = {
            'update_experience' : update_experience,
            'cities' : cities,
            'states' : states
        }
        return render(request,'candidate/update_form/experience_form.html',context)
    
    if 'update_project' in request.path:
        if request.method == 'POST':
            project_name = request.POST.get('project_name')
            associate = request.POST.get('associate')
            project_url = request.POST.get('project_url')
            role = request.POST.get('role')
            role_description = request.POST.get('role_description')
            workplace_type = request.POST.get('workplace_type')
            currently_working = bool(request.POST.get('currently_working'))
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            description = request.POST.get('description')

            if start_date == '':
                start_date = False
            else:
                start_date = start_date

            if end_date == '':
                end_date = False
            else:
                end_date = end_date

            UserProject.objects.filter(id=id).update(project_name=project_name,associate=associate,
                                                    project_url=project_url,role=role,role_description=role_description,
                                                    start_date=start_date,workplace_type=workplace_type,
                                                    currently_working=currently_working,description=description,
                                                    end_date=end_date)

            return redirect('candidate_detail')

        update_project = UserProject.objects.filter(id=id)
        context = {
            'update_project' : update_project
        }
        return render(request,'candidate/update_form/project_form.html',context)
    
    if 'update_cource' in request.path:
        if request.method == 'POST':
            course_name = request.POST.get('course_name')
            associate = request.POST.get('associate')
            currently_working = bool(request.POST.get('currently_working'))
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            description = request.POST.get('description')

            if start_date == '':
                start_date = False
            else:
                start_date = start_date

            if end_date == '':
                end_date = False
            else:
                end_date = end_date

            UserCourse.objects.filter(id=id).update(course_name=course_name,associate=associate,
                                                    currently_working=currently_working,
                                                    start_date=start_date,description=description,
                                                    end_date=end_date)

            return redirect('candidate_detail')

        update_cource = UserCourse.objects.filter(id=id)
        context = {
            'update_cource' : update_cource
        }
        return render(request,'candidate/update_form/cource_form.html',context)
    
    
    

def canfidate_delete_form(request,id):
    if 'delete_education' in request.path:
        model = UserEducation
    
    if 'delete_experience' in request.path:
        model = UserExperience
    
    if 'delete_project' in request.path:
        model = UserProject    

    if 'delete_cource' in request.path:
        model = UserCourse
    
    if 'delete_skill' in request.path:
        model = UserSkill
      
    if 'delete_language' in request.path:
        model = UserLanguage

    model.objects.filter(id=id).delete()
    return redirect('candidate_detail')

def candidate_detail(request):
    
    candidate_detail = User.objects.prefetch_related(Prefetch('userdetail',queryset=UserDetail.objects.all())).get(username=request.user)
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
