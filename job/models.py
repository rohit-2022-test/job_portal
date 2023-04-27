from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ..options import (
    Job_application_collection,
    Schedule_interview_mode,
    Experience_workplace_type,
    Feedback_status
)

class Base(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateField(blank=True, null=True, default=timezone.now)

    class Meta:
        abstract = True

class Job(Base):
    pass

class InterviewSchedule(Base):
    scheduler_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
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
        return f'{self.job_id}'
    
    class Meta:
        db_table = "interview_schedule"
        verbose_name_plural = "Interview Schedule"

class feedback(Base):
    schedule_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
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
