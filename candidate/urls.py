from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.candidate_detail, name='candidate_detail'),

    #Create Detail Name 
    path('candidate_detail/', views.candidate_create_form, name='candidate_data'),
    path('experiance/', views.candidate_create_form, name='experiance'),
    path('language/', views.candidate_create_form, name='language'),
    path('skill/', views.candidate_create_form, name='skill'),
    path('cource/', views.candidate_create_form, name='cource'),
    path('education/', views.candidate_create_form, name='education'),
    path('project/', views.candidate_create_form, name='project'),

    #Update Form
    path('update_education/<int:id>', views.candidate_update_form, name='update_education'),
    path('update_experience/<int:id>', views.candidate_update_form, name='update_experience'),
    path('update_project/<int:id>', views.candidate_update_form, name='update_project'),
    path('update_cource/<int:id>', views.candidate_update_form, name='update_cource'),
    

    #Delete Form
    path('delete_education/<int:id>', views.canfidate_delete_form, name='delete_education'),
    path('delete_experience/<int:id>', views.canfidate_delete_form, name='delete_experience'),
    path('delete_project/<int:id>', views.canfidate_delete_form, name='delete_project'),
    path('delete_cource/<int:id>', views.canfidate_delete_form, name='delete_cource'),
    path('delete_skill/<int:id>', views.canfidate_delete_form, name='delete_skill'),
    path('delete_language/<int:id>', views.canfidate_delete_form, name='delete_language'),
]
