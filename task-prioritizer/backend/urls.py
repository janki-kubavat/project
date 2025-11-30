# backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # accounts pages (login, register)
    path("accounts/", include("accounts.urls")),
    # root -> tasks app (index, saved, export)
    path("", include("tasks.urls")),
]
