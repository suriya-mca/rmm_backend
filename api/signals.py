# api/signals.py

from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import APILog

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """
    Log user login events
    """
    APILog.objects.create(
        user=user,
        endpoint='/api/login/',  # Adjust based on your login endpoint
        method='POST',
        request_data={'username': user.email},
        response_data={'status': 'success', 'message': 'User logged in'}
    )

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    """
    Log user logout events
    """
    APILog.objects.create(
        user=user,
        endpoint='/api/logout/',  # Adjust based on your logout endpoint
        method='POST',
        request_data={'username': user.email},
        response_data={'status': 'success', 'message': 'User logged out'}
    )
