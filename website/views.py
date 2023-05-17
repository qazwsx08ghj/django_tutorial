from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as user_login
from .forms import UserRegisterForm, postContentForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import post
# Create your views here.


def main(request):
    posts = post.objects.all()

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


def postContent(request):
    if request.method == 'POST':
        postCreateForm = postContentForm(request.POST)
        if postCreateForm.is_valid():
            postCreate = postCreateForm.save(commit=False)
            postCreate.user = request.user
            postCreate.save()
            return redirect('/')
        else:
            print(postCreateForm.cleaned_data)
    return render(request, 'postcontent.html')


