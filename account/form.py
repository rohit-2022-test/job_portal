from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'LoginPassword','type':'password','class':'form-input mt-1 rounded-md', 'placeholder':'Password:'}),help_text="Your password must contain at least 8 characters.",error_messages={
            'password_mismatch': 'The two password fields didn\'t match.',
            'min_length': 'Your password must be at least 8 characters long.',
            'numeric_only': 'Your password cannot be entirely numeric.'
        })
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'LoginPassword','type':'password','class':'form-input mt-1 rounded-md', 'placeholder':'Password:'}),help_text="Enter the same password as before,for verification.")

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={'id':'RegisterName', 'type':'text', 'class':'form-input mt-1 rounded-md', 'placeholder':'Enter username'}),
            'email' : forms.EmailInput(attrs={'id':'LoginEmail', 'type':'email','class':'form-input mt-1 rounded-md', 'placeholder':'name@example.com','required':True}),     
        }
