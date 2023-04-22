from django.shortcuts import render, redirect
from .form import SignupForm
from django.contrib import messages

auth_page = 'account/auth.html'

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, auth_page, context)

def login(request):
    return render(request, auth_page)

def reset_password(request):
    return render(request, auth_page)