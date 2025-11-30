from rest_framework import serializers
from .models import Task

class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id_text','title','due_date','estimated_hours','importance','dependencies','created_at','updated_at']
        read_only_fields = ['created_at','updated_at']
