from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)

# User Model
class UserDataAdmin(UserAdmin):
    readonly_fields = [
        "date_joined",
        "last_login",
    ]
    
    # Update Queryset
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        is_superuser = request.user.is_superuser
        if is_superuser:
            if "Super Admin" in request.user.last_name:
                return queryset
            else:
                return queryset.exclude(username='swapnil')
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

