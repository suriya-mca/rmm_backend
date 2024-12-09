import os
from django.core.wsgi import get_wsgi_application

"""
WSGI configuration for deploying the RMM application.
Defines the application entry point for WSGI servers.
"""

# Set the Django settings module path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rmm_core.settings')

# Initialize WSGI application
application = get_wsgi_application()