from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from softdelete.models import SoftDeleteModel
from ckeditor.fields import RichTextField
from options import (
    Job_application_collection,
    Schedule_interview_mode,
    Experience_workplace_type,
    Experience_job_type,
    Feedback_status
)
from company.models import Company
from master_table.models import (
    Location,
    Skill
)

data = '''
<b>Tips:</b> Provide a summary of the role, what success in the position looks like, and how this role fits into the organization overall.<br>

<b>Responsibilities</b>

<p>[Be specific when describing each of the responsibilities. Use gender-neutral, inclusive language.]<br>

Example: Determine and develop user requirements for systems in production, to ensure maximum usability</p>

<b>Qualifications</b>

<p>[Some qualifications you may want to include are Skills, Education, Experience, or Certifications.]<br>

Example: Excellent verbal and written communication skills</p>
'''

class Base(models.Model):
    candidate_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateField(blank=True, null=True, default=timezone.now)

    class Meta:
        abstract = True

class Job(Base, SoftDeleteModel):
    candidate_id = None
    creater_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)
    job_title = models.CharField(max_length=255, blank=False, null=False)
    salary = models.IntegerField(blank=False, null=False)
    experiance = models.CharField(max_length=100, blank=False, null=False)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=False)
    job_type = models.CharField(max_length=100, choices=Experience_job_type, default='frelance')
    workplace_type = models.CharField(max_length=50, choices=Experience_workplace_type, default='on-site')
    datails = RichTextField(default=data,blank=False)
    applicants_collection_mode = models.CharField(max_length=50, choices=Job_application_collection, default='email')
    applicants_collection_link_email = models.CharField(max_length=255, blank=False, null=False)
    applicants_limit = models.IntegerField(blank=False, null=False, default=15)
    skill = models.ManyToManyField(Skill)

    @property
    def compane_name(self):
        return self.company_id

    def __str__(self):
        return f'{self.job_title}'
    
    class Meta:
        db_table = "job"
        verbose_name_plural = "Jobs"

class JobApplicants(Base):
    updated_at = None
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.candidate_id.username}'
    
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

class Feedback(Base):
    schedule_id = models.ForeignKey(InterviewSchedule, on_delete=models.CASCADE, blank=False, null=False)
    description = models.TextField(blank=False)
    status = models.CharField(max_length=10, choices=Feedback_status, default='none')

    def __str__(self):
        if self.status == 'selected':
            return f'{self.candidate_id.username} (Selected)'
        elif self.status == 'rejected':
            return f'{self.candidate_id.username} (Rejected)'
        else:
            return f'{self.candidate_id.username} (Pending)'

    class Meta:
        db_table = "interview_feedback"
        verbose_name_plural = "Interview Feedback"
