# api/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Machine, Command, MachineLog, APILog

class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for User model with email-based authentication.
    """
    model = User
    list_display = ('email', 'api_key', 'is_active', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'api_key')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    readonly_fields = ('api_key',)

class MachineAdmin(admin.ModelAdmin):
    """
    Admin configuration for Machine model with status tracking.
    """
    list_display = ('name', 'status', 'ip_address', 'last_seen')
    list_filter = ('status',)
    search_fields = ('name', 'ip_address')
    readonly_fields = ('last_seen', 'created_at')

class CommandAdmin(admin.ModelAdmin):
    """
    Admin configuration for Command model with execution tracking.
    """
    list_display = ('command_type', 'machine', 'status', 'created_by', 'created_at')
    list_filter = ('command_type', 'status')
    search_fields = ('machine__name', 'created_by__email')
    readonly_fields = ('created_at', 'updated_at')

class MachineLogAdmin(admin.ModelAdmin):
    """
    Admin configuration for MachineLog model with severity levels.
    """
    list_display = ('machine', 'level', 'message', 'created_at')
    list_filter = ('level', 'machine')
    search_fields = ('machine__name', 'message')
    readonly_fields = ('created_at',)

class APILogAdmin(admin.ModelAdmin):
    """
    Admin configuration for APILog model with request tracking.
    """
    list_display = ('timestamp', 'method', 'endpoint', 'user')
    list_filter = ('method', 'endpoint')
    search_fields = ('endpoint', 'user__email')
    readonly_fields = ('timestamp', 'request_data', 'response_data')

# Register models with their custom admin classes
admin.site.register(User, CustomUserAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Command, CommandAdmin)
admin.site.register(MachineLog, MachineLogAdmin)
admin.site.register(APILog, APILogAdmin)