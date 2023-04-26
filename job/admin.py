from django.contrib import admin
from .models import Job, JobApplicants, InterviewSchedule, Feedback
# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.is_staff:
            return qs.filter(user_id=request.user) 


class JobAdmin(BaseAdmin):
    list_display = ['id', 'company_id', 'job_title', 'location_id', 'job_type']
    search_fields = ('company_id', 'job_title')
    list_filter = ('company_id', 'job_title', 'location_id')
    list_display_links = ('company_id',)
    list_per_page = 30

admin.site.register(Job, JobAdmin)

class JobApplicantsAdmin(BaseAdmin):
    list_display = ['id', 'user_id', 'job_id']
    search_fields = ('user_id', 'job_id',)
    list_filter = ('user_id', 'job_id',)
    list_display_links = ('job_id',)
    list_per_page = 30

admin.site.register(JobApplicants, JobApplicantsAdmin)

class InterviewScheduleAdmin(BaseAdmin):
    list_display = ['id', 'scheduler_id', 'job_id']
    search_fields = ('scheduler_id', 'job_id',)
    list_filter = ('scheduler_id', 'job_id',)
    list_display_links = ('scheduler_id', 'job_id',)
    list_per_page = 30

admin.site.register(InterviewSchedule, InterviewScheduleAdmin)

class FeedbackAdmin(BaseAdmin):
    list_display = ['id', 'user_id', 'schedule_id']
    search_fields = ('user_id', 'schedule_id',)
    list_filter = ('user_id', 'schedule_id',)
    list_display_links = ('user_id', 'schedule_id',)
    list_per_page = 30

admin.site.register(Feedback, FeedbackAdmin)