# tasks/views.py
from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import Task  # if not present, create a simple model, or comment out

def index(request):
    return render(request, "index.html")

def saved_tasks(request):
    # if Task model exists:
    try:
        tasks = Task.objects.all()
    except Exception:
        tasks = []
    return render(request, "tasks_saved.html", {"tasks": tasks})

def export_tasks_csv(request):
    # exports CSV with safe fallback if no Task model
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="tasks.csv"'
    writer = csv.writer(response)
    writer.writerow(["id", "title", "priority"])
    try:
        for t in Task.objects.all():
            writer.writerow([t.id, getattr(t, "title", ""), getattr(t, "priority", "")])
    except Exception:
        # no model defined — send header only
        pass
    return response
