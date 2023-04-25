from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:pk>', views.CandidateView.as_view(), name='candidate_detail'),
    path('experiance/', views.candidate_form, name='experiance'),
    path('languege/', views.candidate_form, name='language'),
    path('cource/', views.candidate_form, name='cource'),
    path('education/', views.candidate_form, name='education'),
    path('project/', views.candidate_form, name='project'),
]