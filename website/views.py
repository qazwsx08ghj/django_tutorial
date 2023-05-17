from django.shortcuts import render, redirect, get_object_or_404
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


def myPage(request):
    posts = post.objects.filter(user=request.user)
    return render(request, 'mypage.html', {"posts": posts})


def deleteContent(request, id):
    deletePost = get_object_or_404(post, id=id)
    if request.method == 'GET':
        deletePost.delete()
        return redirect('mypage')
    return redirect('mypage')


def updateContent(request, id):
    updatePost = get_object_or_404(post, id=id)

    if request.method == 'POST':
        updatePost = postContentForm(request.POST, instance=updatePost)
        if updatePost.is_valid():
            updatePost.save()
        return redirect('/mypage')
    return render(request, 'updatecontent.html', {"updatepost": updatePost})

