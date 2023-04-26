from django.contrib import admin
from .models import Company,Comapany_images

# Register your models here.
class CompanyImageInline(admin.TabularInline):
    model = Comapany_images


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'name', 'email', 'phone_no']
    search_fields = ('name', 'location_id')
    list_filter = ('user_id', 'name', 'location_id')
    list_display_links = ('name',)
    list_per_page = 30

    inlines = [
        CompanyImageInline,
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.is_staff:
            return qs.filter(user_id=request.user)  
        
admin.site.register(Company, CompanyAdmin)

