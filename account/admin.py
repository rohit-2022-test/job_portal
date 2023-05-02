from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from admin_dd_filter import RoleListFilter
from django.utils.html import format_html
from .models import UserDetail

# User Model
admin.site.unregister(User)
class UserDataAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "role", "active_candidate")
    list_per_page = 30
    
    # Active Candidate
    def active_candidate(self, obj):
        active_candidate = User.objects.filter(username=obj)
        for role in active_candidate:
            result = format_html("<b style=\"color:MediumSeaGreen;\">Active</b>") if role.is_active else format_html("<b style=\"color:Tomato;\">Inactive</b>")
        return result

    # Role
    def role(self, obj):
        user_role = User.objects.filter(username=obj)
        for role in user_role:
            result = "Admin" if role.is_superuser else "Recruiter" if role.is_staff else "Candidate"
        return format_html("<b>{}</b>", result)

    # Update Filter
    def get_list_filter(self, request):
        if request.user.is_superuser:
            return (RoleListFilter, "groups", "is_active")
        else:
            return []

    # Update Search
    def get_search_fields(self, request):
        if request.user.is_superuser:
            return ("username", "first_name", "last_name", "email")
        else:
            return []

    # Update Read Only Field
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ("date_joined","last_login")
        else:
            return ("groups","user_permissions","date_joined","last_login")

    # Update Queryset
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        is_superuser = request.user.is_superuser
        super_admin = "Super Admin"
        if is_superuser:
            if super_admin in request.user.last_name:
                return queryset
            else:
                return queryset.exclude(last_name__contains =super_admin)
        else:
            return queryset.filter(username=request.user)  
    
    # Disable Form Field
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Change Field Name
        if "add" not in request.path:
            form.base_fields["is_superuser"].label = "admin"
            form.base_fields["is_staff"].label = "recruiter"

        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'username',
                "is_active",
                "is_staff",
                "is_superuser",
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

admin.site.register(User, UserDataAdmin)

'''
Remove the candidate detail from admin panel
'''

# Candidate Detail
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ("candidate_name", "phone_no", "location", "industry", "active_candidate")
    list_per_page = 30

    # Active Candidate
    def active_candidate(self, obj):
        active_candidate = User.objects.filter(username=obj, is_staff=False, is_superuser=False)
        for role in active_candidate:
            result = format_html("<b style=\"color:MediumSeaGreen;\">Active</b>") if role.is_active else format_html("<b style=\"color:Tomato;\">Inactive</b>")
        return result

    # Location
    def location(self, obj):
        instance = User.objects.get(username=obj)
        candidate_location = UserDetail.objects.filter(user_id=instance)
        for location in candidate_location:
            result = location.location_id
        return format_html("<b>{}({})</b>", result.city,(result.state))

    # Update Permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(UserDetail, UserDetailAdmin)

# Group Model
admin.site.unregister(Group)
class GroupDataAdmin(GroupAdmin):

    # Update Permission
    def has_add_permission(self, request, obj=None):
        request_user = request.user.last_name
        super_admin = "Super Admin"

        if super_admin not in request_user:
            return False
        else:
            return True

    def has_change_permission(self, request, obj=None):
        request_user = request.user.last_name
        super_admin = "Super Admin"

        if super_admin not in request_user:
            return False
        else:
            return True
        
    def has_delete_permission(self, request, obj=None):
        request_user = request.user.last_name
        super_admin = "Super Admin"

        if super_admin not in request_user:
            return False
        else:
            return True
        
admin.site.register(Group, GroupDataAdmin)
