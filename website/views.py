from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as user_login
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def main(request):
    posts = {'title': 'Title', 'content': 'Content'}, {'title': 'Title2', 'content': 'Content2'}

    return render(request, 'home.html', {"posts": posts})


def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        LoginForm = AuthenticationForm(data=request.POST)
        if LoginForm.is_valid():
            name = LoginForm.cleaned_data.get('username')
            password = LoginForm.cleaned_data.get('password')
            user = authenticate(username=name, password=password)
            if user is not None:
                user_login(request, user)
                return redirect('/')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        registerForm = UserRegisterForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save()
            user_login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/')
        else:
            print("error")

    return render(request, 'register.html')


def logOut(request):
    logout(request)
    return redirect('/')
