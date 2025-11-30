from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id_text','title','importance','estimated_hours','updated_at')
    search_fields = ('id_text','title')
