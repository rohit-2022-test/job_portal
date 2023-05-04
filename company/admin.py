from django.contrib import admin
from .models import Company,ComapanyImages
from admin_dd_filter import CreatedByFilter, LocationFilter
from django.utils.html import format_html

# Company Image Models
class CompanyImageInline(admin.TabularInline):
    readonly_fields = [
        "created_at",
    ]
    model = ComapanyImages

# Company Models
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'compane_name', 'email', 'phone_no', "location"]
    search_fields = ('name',)
    list_display_links = ('compane_name',)
    list_per_page = 30
    inlines = [CompanyImageInline]
    readonly_fields = ["user_id","created_at","updated_at","deleted_at"]

    # Location
    def location(self, obj):
        company_location = Company.objects.filter(name=obj)
        for location in company_location:
            result = location.location_id
        return format_html("<b>{}({})</b>", result.city,(result.state))

    # Update Filter
    def get_list_filter(self, request):
        if request.user.is_superuser:
            return (CreatedByFilter,"created_at", LocationFilter)
        else:
            return ("created_at", LocationFilter)

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
        request_user = request.user.last_name
        super_admin = "Super Admin"

        if super_admin in request_user:
            return False
        else:
            return True

    def has_change_permission(self, request, obj=None):
        request_user = request.user.last_name
        super_admin = "Super Admin"

        if super_admin in request_user:
            return False
        else:
            return True
        
    def has_delete_permission(self, request, obj=None):
        request_user = request.user.last_name
        super_admin = "Super Admin"

        if super_admin in request_user:
            return False
        else:
            return True

admin.site.register(Company, CompanyAdmin)
