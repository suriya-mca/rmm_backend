from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Machine, Command, MachineLog, APILog

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'api_key', 'is_active', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'api_key')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    readonly_fields = ('api_key',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Machine)
admin.site.register(Command)
admin.site.register(MachineLog)
admin.site.register(APILog)
