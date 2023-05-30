import django_filters
from django import forms
from job.models import Job
from master_table.models import Location
from options import Experience_job_type

class JobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'name':"name", 'type':"text", 'id':"job-keyword", 'class':"form-input filter-input-box bg-gray-50 dark:bg-slate-800 border-0", 'placeholder':"Search your Keywords"}))
  
    location_id = django_filters.ModelChoiceFilter(queryset=Location.objects.all(),widget=forms.Select(attrs={'class':"form-select", 'data-trigger name':"choices-location",'id':"choices-location", 'aria-label':"Default select example"}))
    job_type = django_filters.ChoiceFilter(choices=Experience_job_type,lookup_expr='icontains',widget=forms.Select(attrs={'class':"form-select", 'data-trigger name':"choices-type", 'id':"choices-type", 'aria-labe':"Default select example"}))

    class Meta:
        model = Job
        fields = ['job_title','location_id','job_type']