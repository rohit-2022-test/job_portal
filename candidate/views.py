from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

# Create your views here.
class CandidateView(DetailView):
    template_name = 'candidate/candidate_detail.html'
    model = User

def candidate_form(request):
    if 'languege' in request.path:
        return render(request,'candidate/languege.html')
    if 'project' in request.path:
        return render(request,'candidate/project.html')
    if 'education' in request.path:
        return render(request,'candidate/education.html')
    if 'experiance' in request.path:
        return render(request,'candidate/experiance.html')
    if 'cource' in request.path:
        return render(request,'candidate/cource.html')