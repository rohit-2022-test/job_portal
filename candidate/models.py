from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from master_table.models import (
    Language,
    Skill,
    Location,
)
from .options import (
    language_proficiency,
    Experience_job_type,
    Experience_workplace_type
)

class Base(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    start_date = models.DateField(blank=True, null=True, default=timezone.now)
    end_date = models.DateField(blank=True, null=True, default=timezone.now)
    description = models.TextField(blank=True)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateField(blank=True, null=True, default=timezone.now)
    currently_working = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        abstract = True

class UserLanguage(Base):
    start_date = None
    end_date = None
    description = None
    updated_at = None
    currently_working = None
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, blank=False, null=False)
    proficiency = models.CharField(max_length=50, choices=language_proficiency, default='elementary')

    def __str__(self):
        return f'{self.language_id.name}'
    
    class Meta:
        db_table = "user_language"
        verbose_name_plural = "User Language"

class UserSkill(Base):
    start_date = None
    end_date = None
    description = None
    updated_at = None
    currently_working = None
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE, blank=False, null=False)
    skill_rate = models.IntegerField(default=1, blank=False, null=False)

    def __str__(self):
        return f'{self.skill_id.name}'
    
    class Meta:
        db_table = "user_skill"
        verbose_name_plural = "User Skill"

class UserExperience(Base):
    company_name = models.CharField(max_length=255, blank=False, null=False)
    job_title = models.CharField(max_length=255, blank=False, null=False)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=False)
    skill_rate = models.IntegerField(default=1, blank=False, null=False)
    job_type = models.CharField(max_length=100, choices=Experience_job_type, default='frelance')
    workplace_type = models.CharField(max_length=50, choices=Experience_workplace_type, default='on-site')


    def __str__(self):
        return f'{self.company_name}'
    
    class Meta:
        db_table = "user_experience"
        verbose_name_plural = "User Experience"

class UserEducation(Base):
    currently_working = None
    institute_name = models.CharField(max_length=255, blank=False, null=False)
    course = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    grade = models.CharField(max_length=5, blank=False, null=False)
    activities = models.TextField(blank=True)

    def __str__(self):
        return f'{self.institute_name}'
    
    class Meta:
        db_table = "user_education"
        verbose_name_plural = "User Education"

class UserCourse(Base):
    start_date = None
    end_date = None
    currently_working = None
    course_name = models.CharField(max_length=255, blank=False, null=False)
    associate = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.course_name}'
    
    class Meta:
        db_table = "user_course"
        verbose_name_plural = "User Course"

class UserProject(Base):
    experiance_id = models.ForeignKey(UserExperience, on_delete=models.CASCADE, blank=False, null=False)
    project_name = models.CharField(max_length=255, blank=False, null=False)
    associate = models.CharField(max_length=255, blank=True, null=True)
    project_url = models.CharField(max_length=255, blank=False, null=False)
    workplace_type = models.CharField(max_length=50, choices=Experience_workplace_type, default='on-site')
    role = models.CharField(max_length=100, blank=False, null=False)
    role_description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.project_name}'
    
    class Meta:
        db_table = "user_project"
        verbose_name_plural = "User Project"
