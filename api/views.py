# api/views.py

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Machine, MachineLog
from .serializers import MachineSerializer, MachineLogSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def machine_list(request):
    """
    List all machines or create a new machine.
    
    GET: Returns list of all machines
    POST: Creates a new machine
    """
    if request.method == 'GET':
        # Get all machines from database
        machines = Machine.objects.all()
        # Serialize the machines data
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create new machine from posted data
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def machine_detail(request, machine_id):
    """
    Retrieve, update or delete a machine.
    
    GET: Returns details of specific machine
    PUT: Updates machine details
    DELETE: Removes machine from system
    """
    # Get machine object or return 404
    machine = get_object_or_404(Machine, id=machine_id)

    if request.method == 'GET':
        serializer = MachineSerializer(machine)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MachineSerializer(machine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        machine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_machine_status(request, machine_id):
    """
    Update the status of a specific machine.
    
    POST: Updates machine status (online/offline/maintenance)
    """
    machine = get_object_or_404(Machine, id=machine_id)
    
    # Get status from request data
    new_status = request.data.get('status')
    
    # Validate status
    if new_status not in [choice[0] for choice in Machine.STATUS_CHOICES]:
        return Response(
            {'error': 'Invalid status. Choose from: online, offline, maintenance'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Update machine status
    machine.status = new_status
    machine.save()
    
    serializer = MachineSerializer(machine)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def machine_logs(request, machine_id):
    """
    List all logs for a specific machine or create a new log entry.
    
    GET: Returns list of logs for the machine
    POST: Creates a new log entry for the machine
    """
    machine = get_object_or_404(Machine, id=machine_id)

    if request.method == 'GET':
        logs = MachineLog.objects.filter(machine=machine)
        serializer = MachineLogSerializer(logs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Add machine to request data
        data = request.data.copy()
        data['machine'] = machine.id
        
        serializer = MachineLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)