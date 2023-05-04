from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

from pages.form import ContactForm
from pages.models import Contact

def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about_us.html')

def contact(request):

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            usermessage = form.cleaned_data.get('message')
            name = form.cleaned_data.get('name')
            subject = form.cleaned_data.get('subject')
            email = form.cleaned_data.get('email')
            date_of_request = Contact.objects.filter(name=name).values_list('created_at',flat=True).last()
            send_mail(
                'Ecommerce Inquiry',
                f"There has been an inquiry for {subject}. Name: {name} ,Message: {usermessage}. Date: {date_of_request}.'",
                'joshijaya.shivinfotech@gmail.com',
                ('joshijaya29@gmail.com',),
                fail_silently=False
                ) 
            send_mail(
                'Your Inquiry is Submmited.',
                f"There has been an inquiry for {subject}.Message: {usermessage}.'",
                'joshijaya.shivinfotech@gmail.com',
                [email,],
                fail_silently=False
                )  
            messages.success(request, 'Your inquery is on processed')  
            return redirect('index')
        else:
            messages.error(request, 'Please Enter conrrect data.')  
            return redirect('contact')
    
    context = {
        'form' : form
        }
    return render(request,'pages/contact.html',context)

