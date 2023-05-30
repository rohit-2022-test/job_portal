from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Pages
    path('',include('pages.urls')),

    # Account
    path('accounts/',include('account.urls')),

    # Candidate
    path('candidate/',include('candidate.urls')),

    # Job
    path('job/',include('job.urls')),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
