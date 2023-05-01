from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.candidate_detail, name='candidate_detail'),
    path('experiance/', views.candidate_create_form, name='experiance'),
    path('language/', views.candidate_create_form, name='language'),
    path('skill/', views.candidate_create_form, name='skill'),
    path('cource/', views.candidate_create_form, name='cource'),
    path('education/', views.candidate_create_form, name='education'),
    path('project/', views.candidate_create_form, name='project'),
    path('update_education/<int:id>', views.candidate_update_form, name='update_education'),
    path('update_experience/<int:id>', views.candidate_update_form, name='update_experience'),
    path('update_project/<int:id>', views.candidate_update_form, name='update_project'),
    path('update_cource/<int:id>', views.candidate_update_form, name='update_cource'),
    path('update_skill/<int:id>', views.candidate_update_form, name='update_skill'),
    path('update_language/<int:id>', views.candidate_update_form, name='update_language'),
]
