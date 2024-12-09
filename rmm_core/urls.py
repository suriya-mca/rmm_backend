from django.contrib import admin
from django.urls import path, include

"""
Root URL configuration for the RMM (Remote Machine Management) project.
Includes admin interface and API routes.
"""

urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),
    
    # API endpoints under version 1
    path('api/v1/', include('api.urls')),
]