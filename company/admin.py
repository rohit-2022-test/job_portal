from django.contrib import admin
from .models import Company,ComapanyImages
from admin_dd_filter import RecruiterListFilter

# Company Image Models
class CompanyImageInline(admin.TabularInline):
    readonly_fields = [
        "created_at",
    ]
    model = ComapanyImages

# Check Super Admin
def is_superadmin_check(data):
    request_user = data.user.last_name
    super_admin = "Super Admin"

    if super_admin in request_user:
        return False
    else:
        return True

# Company Models
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'name', 'email', 'phone_no']
    search_fields = ('name',)
    list_filter = (RecruiterListFilter,)
    list_display_links = ('name',)
    list_per_page = 30
    inlines = [CompanyImageInline]

    readonly_fields = ["user_id","created_at","updated_at","deleted_at"]

    # Update Queryset
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        is_superuser = request.user.is_superuser
        if is_superuser:
            return queryset
        else:
            return queryset.filter(user_id=request.user)

    # Update Save request
    def save_model(self, request, instance, form, *args):
        user = request.user
        instance = form.save(commit=False)
        instance.user_id = user
        instance.save()
        form.save_m2m()
        return instance

    # Data edit Permission
    def has_add_permission(self, request, obj=None):
        is_superadmin_check(request)

    def has_change_permission(self, request, obj=None):
        is_superadmin_check(request)
        
    def has_delete_permission(self, request, obj=None):
        is_superadmin_check(request)

admin.site.register(Company, CompanyAdmin)
