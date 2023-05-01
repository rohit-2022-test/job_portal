from django.contrib import admin
from candidate.models import (
    UserEducation,
    UserCourse,
    UserExperience,
    UserLanguage,
    UserProject,
    UserSkill
)

# Company Image Models
class CompanyImageInline(admin.TabularInline):
    pass
