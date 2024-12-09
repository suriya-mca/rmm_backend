from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Machine, Command, MachineLog

class CustomUserAdmin(UserAdmin):
    model = User
    # Specify fields to display
    list_display = ('email', 'api_key', 'is_active', 'is_staff')
    # Specify fields for search functionality
    search_fields = ('email',)
    ordering = ('email',)
    # Define the fieldsets for user creation and editing
    fieldsets = (
        (None, {'fields': ('email', 'password', 'api_key')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    readonly_fields = ('api_key',)  # Prevent editing of `api_key`

admin.site.register(User, CustomUserAdmin)
admin.site.register(Machine)
admin.site.register(Command)
admin.site.register(MachineLog)
