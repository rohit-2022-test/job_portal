from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import Q
from master_table.models import Location

# Role Filter
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

# Queryset
def query_user_data():
    user_data = User.objects.filter(Q(is_superuser = True) | Q(is_staff = True)).exclude(last_name__contains="Super Admin").values_list('username', 'id')
    return user_data

# Created By Filter
class CreatedByFilter(admin.SimpleListFilter):
    title = _("created by filter")
    parameter_name = "created by"

    def lookups(self, request, model_admin):
        dropdown_options = [(key[0], _(key[0])) for key in query_user_data()]
        return dropdown_options

    def queryset(self, request, queryset):
        for qd in query_user_data():
            if self.value() == qd[0]:
                try:
                    return queryset.filter(user_id=qd[1])
                except Exception:
                    return queryset.filter(creater_id=qd[1])

# Queryset
def query_state_data():
    location_data = Location.objects.all().distinct().values_list('state')
    return location_data

# Location Filter
class LocationFilter(admin.SimpleListFilter):
    title = _("state filter")
    parameter_name = "state"

    def lookups(self, request, model_admin):
        dropdown_options = [(key[0], _(key[0])) for key in query_state_data()]
        return dropdown_options

    def queryset(self, request, queryset):
        for qd in query_state_data():
            if self.value() == qd[0]:
                return queryset.filter(location_id__state=qd[0])
        
# Salary Filter
class SalaryFilter(admin.SimpleListFilter):
    title = _("salary filter")
    parameter_name = "salary"

    def lookups(self, request, model_admin):
        dropdown_options = [
            ('10000', _('Less Then 10K')),
            ('10000-50000', _('10K - 50K')),
            ('50000-110000', _('50K - 110K')),
            ('110000', _('More Then 110K')),
        ]
        return dropdown_options

    def queryset(self, request, queryset):
        try:
            data = self.value().split("-")
        except Exception:
            data = [0]
        if self.value() == '10000':
            return queryset.filter(salary__lt = 10000)
        if self.value() == '110000':
            return queryset.filter(salary__gt = 110000)
        if len(data) == 2:
            return queryset.filter(Q(salary__lt = data[1]) & Q(salary__gt = data[0]))
