from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordResetForm,
    SetPasswordForm
)


class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'LoginPassword','type':'password','class':'form-input mt-1 rounded-md', 'placeholder':'Password:'}),
                                help_text="Your password must contain at least 8 characters.")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'LoginPassword','type':'password','class':'form-input mt-1 rounded-md', 'placeholder':'Password:'}),
                                help_text="Enter the same password as before,for verification.")

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={'id':'RegisterName', 'type':'text', 'class':'form-input mt-1 rounded-md', 'placeholder':'Enter username'}),
            'email' : forms.EmailInput(attrs={'id':'LoginEmail', 'type':'email','class':'form-input mt-1 rounded-md', 'placeholder':'name@example.com','required':True}),     
        }

class PasswordReset(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'id':'LoginEmail', 'type':'email' ,'class':'form-input mt-3 rounded-md','placeholde':'name@example.com'}),
    )

class PasswordConfirm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'type':"password", 'name':"password", 'class':"form-input mt-3 rounded-md", 'placeholder':"Password:"}),
        strip=False,
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'type':"password", 'name':"password", 'class':"form-input mt-3 rounded-md", 'placeholder':"Password:"}),
    )
