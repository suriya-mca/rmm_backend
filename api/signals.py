# api/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import APILog

@receiver(post_save, sender=Response)
def log_api_response(sender, instance, created, **kwargs):
    """
    Log DRF Response objects when they are created
    """
    try:
        # Get the request from the response context
        request = instance.renderer_context.get('request')
        
        if request:
            # Create API log entry
            APILog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                endpoint=request.path,
                method=request.method,
                request_data=request.data if hasattr(request, 'data') else None,
                response_data=instance.data if hasattr(instance, 'data') else None
            )
    except Exception as e:
        print(f"Error logging API response: {str(e)}")
