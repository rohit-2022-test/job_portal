import django_filters
from django import forms
from job.models import Job
from django.db.models import Count
from master_table.models import Location
from options import Experience_job_type

class JobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'name':"search", 'id':"searchname", 'type':"text", 'class':"form-input border border-slate-100 dark:border-slate-800 ltr:pl-10 rtl:pr-10", 'placeholde':"Search"}))
    location_id = django_filters.ModelChoiceFilter(queryset=Location.objects.all(),widget=forms.Select(attrs={'class':"form-select form-input border border-slate-100 dark:border-slate-800 block w-full mt-1"}))
    job_type = django_filters.MultipleChoiceFilter(choices=Experience_job_type,lookup_expr='icontains',widget=forms.CheckboxSelectMultiple(attrs={'name':"search", 'id':"searchname", 'type':"checkbox", 'class':"form-checkbox border border-slate-100 dark:border-slate-800 text-emerald-600 rounded w-4 h-4", 'placeholde':"Search"}))
    salary = django_filters.NumberFilter(lookup_expr='icontains',widget=forms.RadioSelect(choices=[
                ('1', '1000 - 5000'),
                ('2', '5000 - 10000'),
                ('3', 'more than 10000')
            ],attrs={'id':"searchname", 'type':"radio", 'class':"form-radio border border-slate-100 dark:border-slate-800 ltr:pl-10 rtl:pr-10", 'placeholde':"Search"}))

    class Meta:
        model = Job
        fields = ['job_title','location_id','job_type','salary']



