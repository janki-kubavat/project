# tasks/urls.py
from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),                       # /
    path("saved/", views.saved_tasks, name="saved_tasks"),     # /saved/
    path("saved/export/", views.export_tasks_csv, name="export_tasks_csv"),  # /saved/export/
]
