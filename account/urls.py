from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView)

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',views.MyLoginView.as_view(template_name='account/auth.html'),name='login'),
    path('password-reset/', PasswordResetView.as_view(template_name='account/auth.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         PasswordResetConfirmView.as_view(
            template_name='account/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
    path('logout/',auth_views.LogoutView.as_view(template_name='account/auth.html'),name='logout'),
]