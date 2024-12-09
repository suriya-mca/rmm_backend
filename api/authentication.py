# api/authentication.py

from rest_framework import authentication
from rest_framework import exceptions
from api.models import User

class APIKeyAuthentication(authentication.BaseAuthentication):
    """
    Custom authentication class that validates API keys provided in the X-API-KEY header.
    Returns None if no API key is provided (allowing other authentication methods to be attempted).
    """
    def authenticate(self, request):
        # Get API key from request headers
        api_key = request.META.get('HTTP_X_API_KEY')
        
        # Skip this authentication method if no API key provided
        if not api_key:
            return None

        try:
            # Look up user by API key and return tuple of (user, auth)
            user = User.objects.get(api_key=api_key)
            return (user, None)
        except User.DoesNotExist:
            # Raise authentication error if API key is invalid
            raise exceptions.AuthenticationFailed('Invalid API key')