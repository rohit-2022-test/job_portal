from django import forms
from django.forms import ModelForm
from candidate.models import UserExperience
from master_table.models import Location
from options import Experience_job_type, Experience_workplace_type

def validate_city(value):

    location = Location.objects.filter(city=value)
    if not location.exists():
        raise forms.ValidationError("City does not exist.")


class UserExperienceForm(ModelForm):

    company_name = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'class':"form-input mt-1 rounded-md"}))

    job_title = forms.CharField(widget=forms.TextInput(attrs={'type':"text",'class':"form-input mt-1 rounded-md"}))

    state = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'list':'states', 'class':"form-input mt-1 rounded-md"}))

    city = forms.CharField(validators=[validate_city],widget=forms.TextInput(attrs={'type':"text", 'list':'cities', 'class':"form-input mt-1 rounded-md"}))

    job_type = forms.ChoiceField(choices=Experience_job_type, widget=forms.Select(attrs={'type':"text", 'class':"form-input mt-1 rounded-md"}))

    workplace_type = forms.ChoiceField(choices=Experience_workplace_type,widget=forms.Select(attrs={'type':"text", 'class':"form-input mt-1 rounded-md"}))

    start_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'month', 'class': 'form-input mt-1 rounded-md', 'placeholder': ''}),
        input_formats=['%Y-%m'],
    )
    end_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'month', 'class': 'form-input mt-1 rounded-md', 'placeholder': ''}),
        input_formats=['%Y-%m'],
    )
    currently_working = forms.BooleanField(initial=False,required=False)
    
    description = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'class':"form-input mt-1 rounded-md", 'placeholder':""}))

    class Meta:
        model = UserExperience
        fields = ['company_name','job_title','job_type','workplace_type','state',
                  'city','description','currently_working','start_date','end_date']