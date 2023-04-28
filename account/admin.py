from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from admin_dd_filter import RoleListFilter

# User Model
admin.site.unregister(User)
class UserDataAdmin(UserAdmin):
    readonly_fields = [
        "date_joined",
        "last_login",
    ]

    # Update Filter
    def get_list_filter(self, request):
        if request.user.is_superuser:
            return (RoleListFilter, "groups")
        else:
            return []

    # Update Search
    def get_search_fields(self, request):
        if request.user.is_superuser:
            return ("username", "first_name", "last_name", "email")
        else:
            return []

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

# Group Model
admin.site.unregister(Group)
class GroupDataAdmin(GroupAdmin):

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
