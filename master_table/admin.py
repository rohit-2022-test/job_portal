from django.contrib import admin
from .models import (
    Industry,
    Designation,
    Language,
    Skill,
    Location,
    PgCourse,
    PgSubject,
    UgCourse,
    UgSubject
)

class UgSubjectInline(admin.TabularInline):
    model = UgSubject

class PgSubjectInline(admin.TabularInline):
    model = PgSubject

@admin.action(description="Not display Selected Items")
def not_display(modeladmin, request, queryset):
    queryset.update(is_disple = False)

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'is_display']
    list_per_page = 30
    list_filter = ('is_display',)
    actions = [not_display]

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'is_display']
    list_per_page = 30
    list_filter = ('is_display',)
    actions = [not_display]

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'is_display']
    list_per_page = 30
    list_filter = ('is_display',)
    actions = [not_display]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'is_display']
    list_per_page = 30
    list_filter = ('is_display',)
    actions = [not_display]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','city', 'state', 'is_display']
    list_per_page = 30
    list_filter = ('is_display', 'state')
    actions = [not_display]

@admin.register(UgCourse)
class UgCourseAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'is_display']
    list_per_page = 30
    list_filter = ('is_display',)
    actions = [not_display]
    inlines = [UgSubjectInline]

@admin.register(PgCourse)
class PgCourseAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'is_display']
    list_per_page = 30
    list_filter = ('is_display',)
    actions = [not_display]
    inlines = [PgSubjectInline]
