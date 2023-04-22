from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'account/auth.html')

def login(request):
    return render(request,'account/auth.html')

def reset_password(request):
    return render(request,'account/auth.html')