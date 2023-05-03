from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    
    path('login/',views.MyLoginView.as_view(template_name=views.auth_page),
         name='login'),

    path('password-reset/',
         views.PasswordReset.as_view(template_name=views.auth_page),
         name='password-reset'),
    
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
    template_name='account/password_reset_done.html'),
    name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         views.PasswordConfirm.as_view(
    template_name='account/password_reset_confirm.html'),
    name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
    template_name='account/password_reset_complete.html'),
    name='password_reset_complete'),

    path('logout/',auth_views.LogoutView.as_view(template_name=views.auth_page),
         name='logout'),
]