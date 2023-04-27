from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import Q

# Filter 
# User Filter
class RoleListFilter(admin.SimpleListFilter):
    title = _("role filter")
    parameter_name = "role"

    def lookups(self, request, model_admin):
        dropdown_options = [
            ('admin', _('admin')),
            ('candidate', _('candidate')),
            ('recruiter', _('recruiter')),
        ]
        return dropdown_options

    def queryset(self, request, queryset):
        if self.value() == 'admin':
            return queryset.filter(is_superuser=True)
        if self.value() == 'recruiter':
            return queryset.filter(is_staff=True, is_superuser=False)
        if self.value() == 'candidate':
            return queryset.filter(is_staff=False, is_superuser=False)


# Company Filter
def query_data():
    user_data = User.objects.filter(Q(is_superuser = True) | Q(is_staff = True)).exclude(last_name__contains="Super Admin").values_list('username', 'id')
    return user_data

class RecruiterListFilter(admin.SimpleListFilter):
    title = _("recruiter filter")
    parameter_name = "recruiter"

    def lookups(self, request, model_admin):
        dropdown_options = [(key[0], _(key[0])) for key in query_data()]
        return dropdown_options

    def queryset(self, request, queryset):
        for qd in query_data():
            if self.value() == qd[0]:
                return queryset.filter(user_id=qd[1])
            