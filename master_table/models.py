from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Base(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    is_display = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)

    class Meta:
        abstract = True

class Industry(Base):
    unimportant_field = None
    
    def __str__(self):
        return f'{self.name} Industry'
    
    class Meta:
        db_table = "industry"
        verbose_name_plural = "Industries"

class Designation(Base):
    unimportant_field = None
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "designation"
        verbose_name_plural = "Designation"

class Language(Base):
    unimportant_field = None
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "language"
        verbose_name_plural = "Languages"

class Skill(Base):
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "skill"
        verbose_name_plural = "Skills"

class Location(models.Model):
    country = models.CharField(max_length=50, default="India", blank=False, null=False)
    state = models.CharField(max_length=150, blank=False, null=False)
    city = models.CharField(max_length=150, blank=False, null=False)
    is_display = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)


    def __str__(self):
        return self.city
    
    class Meta:
        db_table = "location"
        verbose_name_plural = "Locations"

class UgCourse(Base):
    unimportant_field = None
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "ug_course"
        verbose_name_plural = "Undergraduate Courses"

class UgSubject(Base):
    ug_course_id = models.ForeignKey(UgCourse, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "ug_subject"
        verbose_name_plural = "Undergraduate Subject"

class PgCourse(Base):
    unimportant_field = None
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "pg_course"
        verbose_name_plural = "Postgraduate Courses"

class PgSubject(Base):
    pg_course_id = models.ForeignKey(PgCourse, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "pg_subject"
        verbose_name_plural = "Postgraduate Subject"

