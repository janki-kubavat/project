# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_view(request):
    # simple placeholder form handling; if POST you can implement real auth
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("tasks:index")
        messages.error(request, "Invalid credentials")
    return render(request, "login.html", {"form": {}})

def register_view(request):
    # minimal placeholder: show form; you can implement real registration later
    if request.method == "POST":
        # implement user creation here
        messages.success(request, "Account created (placeholder). Please implement.")
        return redirect("accounts:login")
    return render(request, "register.html", {"form": {}})
