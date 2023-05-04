from django.urls import path
from . import views

urlpatterns = [
    path('job_list/', views.job_list, name='job_list'),
    path('job_filter/', views.job_filter, name='job_filter'),
    path('job_detail/<int:id>', views.job_detail, name='job_detail'),
    path('job_apply/', views.job_apply, name='job_apply'),
]