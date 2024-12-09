# api/serializers.py

from rest_framework import serializers
from api.models import Machine, Command, MachineLog

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'name', 'status', 'ip_address', 'last_seen', 'created_at']
        read_only_fields = ['id', 'last_seen', 'created_at']

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ['id', 'machine', 'command_type', 'command_data', 'status', 'created_by', 
                 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

class MachineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLog
        fields = ['id', 'machine', 'level', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']