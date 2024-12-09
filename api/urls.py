# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Machine endpoints
    path('machines/', 
         views.machine_list, 
         name='machine-list'),  # GET: list all machines, POST: create new machine
    
    path('machines/<uuid:machine_id>/', 
         views.machine_detail, 
         name='machine-detail'),  # GET, PUT, DELETE specific machine
    
    path('machines/<uuid:machine_id>/status/', 
         views.update_machine_status, 
         name='machine-status-update'),  # POST: update machine status
    
    path('machines/<uuid:machine_id>/logs/', 
         views.machine_logs, 
         name='machine-logs'),  # GET: list logs, POST: create log
]