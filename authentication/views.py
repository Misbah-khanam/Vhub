from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username-login")
        password = request.POST.get("password-login")
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        login(request, user)
        return redirect('home')
    return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get("username-register")
        password = request.POST.get("password-register")
        confirm_password = request.POST.get("confirm-password-register")
        if(password == confirm_password):
            user = User(
                username = username,
                password = password,
            )
            user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')