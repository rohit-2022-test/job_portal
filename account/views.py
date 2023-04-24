from django.shortcuts import render, redirect
from .form import SignupForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView,LoginView,PasswordResetView
from django.urls import reverse_lazy

auth_page = 'account/auth.html'

#Registration
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

#Login
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
