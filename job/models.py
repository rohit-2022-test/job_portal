from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from softdelete.models import SoftDeleteModel
from options import (
    Job_application_collection,
    Schedule_interview_mode,
    Experience_workplace_type,
    Experience_job_type,
    Feedback_status
)
from company.models import Company
from master_table.models import Location

class Base(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateField(blank=True, null=True, default=timezone.now)

    class Meta:
        abstract = True

class Job(Base, SoftDeleteModel):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)
    job_title = models.CharField(max_length=255, blank=False, null=False)
    salary = models.CharField(max_length=20, blank=False, null=False)
    experiance = models.CharField(max_length=100, blank=False, null=False)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=False)
    job_type = models.CharField(max_length=100, choices=Experience_job_type, default='frelance')
    workplace_type = models.CharField(max_length=50, choices=Experience_workplace_type, default='on-site')
    datails = models.TextField(blank=False)
    applicants_collection_mode = models.CharField(max_length=50, choices=Job_application_collection, default='email')
    applicants_collection_link_email = models.CharField(max_length=255, blank=False, null=False)
    applicants_limit = models.IntegerField(blank=False, null=False, default=15)

    def __str__(self):
        return f'{self.job_title}'
    
    class Meta:
        db_table = "job"
        verbose_name_plural = "Jobs"

class JobApplicants(Base):
    updated_at = None
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.user_id.username}'
    
    class Meta:
        db_table = "job_applicants"
        verbose_name_plural = "Job Applicants"

class InterviewSchedule(Base):
    scheduler_id = models.ForeignKey(User, related_name='scheduler_name', on_delete=models.CASCADE, blank=False, null=False)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, blank=False, null=False)
    interview_mode = models.CharField(max_length=10, choices=Schedule_interview_mode, default='online')
    interview_link = models.CharField(max_length=255, blank=False, null=False)
    interview_date = models.DateField(blank=True, null=True)
    interview_time = models.TimeField(blank=True, null=True)
    duration = models.IntegerField(blank=False, null=False, default=15)
    interviewer = models.CharField(max_length=255, blank=False, null=False)
    interview_focus = models.CharField(max_length=255, blank=False, null=False)
    datails = models.TextField(blank=True)

    def __str__(self):
        return f'{self.job_id.job_title}'
    
    class Meta:
        db_table = "interview_schedule"
        verbose_name_plural = "Interview Schedule"

class feedback(Base):
    schedule_id = models.ForeignKey(InterviewSchedule, on_delete=models.CASCADE, blank=False, null=False)
    description = models.TextField(blank=False)
    status = models.CharField(max_length=10, choices=Feedback_status, default='none')

    def __str__(self):
        if self.status == 'selected':
            return f'{self.user_id.username} (Selected)'
        elif self.status == 'rejected':
            return f'{self.user_id.username} (Rejected)'
        else:
            return f'{self.user_id.username} (Pending)'

    class Meta:
        db_table = "interview_feedback"
        verbose_name_plural = "Interview Feedback"
