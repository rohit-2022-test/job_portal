from django.contrib import admin
from admin_dd_filter import CreatedByFilter, LocationFilter, SalaryFilter
from .models import Job, JobApplicants, InterviewSchedule, Feedback
from django.utils.html import format_html

class BaseAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        is_superuser = request.user.is_superuser
        if is_superuser:
            return queryset
        else:
            if "interviewschedule" in request.path:
                return queryset.filter(scheduler_id=request.user) 
            elif "feedback" in request.path:
                return queryset.filter(schedule_id__scheduler_id=request.user)
            elif "job" in request.path:
                return queryset.filter(creater_id=request.user) 

# Job Application
class JobApplicantsInline(admin.StackedInline):
    model = JobApplicants

    # Update Permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class JobAdmin(BaseAdmin):
    list_display = ['id', 'creater_id', 'company_id', 'job_title', 'location', 'job_type', 'salary', "job_applicants"]
    search_fields = ('job_title',)
    list_display_links = ('company_id',)
    readonly_fields = ["creater_id","created_at","updated_at","deleted_at"]
    inlines = [JobApplicantsInline]
    list_per_page = 30

    # Location
    def location(self, obj):
        job_location = Job.objects.filter(job_title=obj)
        for location in job_location:
            result = location.location_id
        return format_html("<b>{}({})</b>", result.city,(result.state))

    # Job applications
    def job_applicants(self, obj):
        total_applicantion = JobApplicants.objects.filter(job_id=obj).count()
        return total_applicantion

    # Update Filter
    def get_list_filter(self, request):
        if request.user.is_superuser:
            return (CreatedByFilter,"created_at", LocationFilter, SalaryFilter)
        else:
            return ("created_at", LocationFilter, SalaryFilter)

    # Update Save request
    def save_model(self, request, instance, form, *args):
        user = request.user
        instance = form.save(commit=False)
        instance.creater_id = user
        instance.save()
        form.save_m2m()
        return instance

    # Data edit Permission
    def has_add_permission(self, request, obj=None):
        request_user = request.user.last_name
        super_admin = "Super Admin"

        if super_admin in request_user:
            return False
        else:
            return True

    def has_change_permission(self, request, obj=None):
        request_user = request.user.last_name
        super_admin = "Super Admin"

        if super_admin in request_user:
            return False
        else:
            return True
        
    def has_delete_permission(self, request, obj=None):
        request_user = request.user.last_name
        super_admin = "Super Admin"

        if super_admin in request_user:
            return False
        else:
            return True

admin.site.register(Job, JobAdmin)

class InterviewScheduleAdmin(BaseAdmin):
    list_display = ['id', 'scheduler_id', 'job_id']
    search_fields = ('scheduler_id', 'job_id',)
    list_filter = ('scheduler_id', 'job_id',)
    list_display_links = ('scheduler_id', 'job_id',)
    list_per_page = 30

admin.site.register(InterviewSchedule, InterviewScheduleAdmin)

class FeedbackAdmin(BaseAdmin):
    list_display = ['id', 'candidate_id', 'schedule_id']
    search_fields = ('candidate_id', 'schedule_id',)
    list_filter = ('candidate_id', 'schedule_id',)
    list_display_links = ('candidate_id', 'schedule_id',)
    list_per_page = 30

admin.site.register(Feedback, FeedbackAdmin)