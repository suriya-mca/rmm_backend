from django.contrib import admin

from .models import User, Machine, Command, MachineLog

admin.site.register(User)
admin.site.register(Machine)
admin.site.register(Command)
admin.site.register(MachineLog)
