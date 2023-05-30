from django import forms

from django.forms import ModelForm
from pages.models import Contact

class ContactForm(ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'name':"name", 'id':"name", 'type':"text", 'class':"form-input mt-2", 'placeholder':"Name :"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':"email", 'id':"email", 'type':"email", 'class':"form-input mt-2", 'placeholder':"Email :"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'name':"subject",'id':"subject", 'class':"form-input mt-2", 'placeholder':"Subject :"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'name':"comments", 'id':"comments", 'class':"form-input mt-2 textarea", 'placeholder':"Message :"}))

    class Meta:
        model = Contact
        fields = ['name','email','subject','message']


