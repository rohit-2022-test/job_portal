from django.contrib import admin
from .models import (
    UserSkill,
    UserCourse,
    UserEducation,
    UserExperience,
    UserLanguage,
    UserProject
)
from account.models import UserDetail

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(UserSkill)
admin.site.register(UserCourse)
admin.site.register(UserEducation)
admin.site.register(UserLanguage)
admin.site.register(UserExperience)
admin.site.register(UserProject)