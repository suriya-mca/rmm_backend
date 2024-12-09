# api/models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings
import uuid

class UserManager(BaseUserManager):
    """
    Custom user manager that handles user and superuser creation with email as the unique identifier.
    """
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user with the given email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and saves a new superuser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    """
    Custom user model using email instead of username.
    Includes an API key for authentication.
    """
    username = None
    email = models.EmailField(unique=True)
    api_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.email

class Machine(models.Model):
    """
    Represents a machine in the system with its current status and network information.
    """
    STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('maintenance', 'Maintenance'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='offline')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    last_seen = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.status})"

class Command(models.Model):
    """
    Stores commands sent to machines with their execution status and metadata.
    """
    COMMAND_TYPES = [
        ('update', 'Update'),
        ('restart', 'Restart'),
        ('shutdown', 'Shutdown'),
        ('custom', 'Custom'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='commands')
    command_type = models.CharField(max_length=20, choices=COMMAND_TYPES)
    command_data = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.command_type} on {self.machine.name}"

class MachineLog(models.Model):
    """
    Stores log entries from machines with different severity levels.
    Ordered by creation time with most recent first.
    """
    LOG_LEVELS = [
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('error', 'Error'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='logs')
    level = models.CharField(max_length=20, choices=LOG_LEVELS, default='info')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.level}: {self.message[:50]}"

class APILog(models.Model):
    """
    Tracks all API requests with request/response data and user information.
    Ordered by timestamp with most recent first.
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    request_data = models.JSONField(null=True)
    response_data = models.JSONField(null=True)
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.method} {self.endpoint} at {self.timestamp}"