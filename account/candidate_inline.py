from django.contrib import admin
from account.models import UserDetail
from candidate.models import (
    UserEducation,
    UserCourse,
    UserExperience,
    UserLanguage,
    UserProject,
    UserSkill
)

# Candidate Details
class CandidateDetailInline(admin.StackedInline):
    model = UserDetail

    # Update Permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
# Candidate Education
class UserEducationInline(admin.StackedInline):
    model = UserEducation

    # Update Permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
# Candidate Course
class UserCourseInline(admin.StackedInline):
    model = UserCourse

    # Update Permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
# Candidate Skill
class UserSkillInline(admin.StackedInline):
    model = UserSkill

    # Update Permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
# Candidate Project
class UserProjectInline(admin.StackedInline):
    model = UserProject

    # Update Permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
# Candidate Language
class UserLanguageInline(admin.StackedInline):
    model = UserLanguage

    # Update Permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
# Candidate Experience
class UserExperienceInline(admin.StackedInline):
    model = UserExperience

    # Update Permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
