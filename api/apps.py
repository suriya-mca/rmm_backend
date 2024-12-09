#api/apps.py

from django.apps import AppConfig

class ApiConfig(AppConfig):
    """
    Configuration class for the API application.
    Handles app initialization and signal registration.
    """
    # Use BigAutoField as the primary key type for all models
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Internal reference name for the application
    name = 'api'
    
    def ready(self):
        """
        Called when the application is ready.
        Imports signal handlers to ensure they are registered.
        """
        import api.signals
