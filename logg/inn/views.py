from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


def home(request):
    print(request.user)
    user = request.user
    return render(request, 'header.html', {'user': user})

def logoutt(request):
    logout(request)
    return render(request, 'header.html')

def log(request):
    if request.POST:
        print(request.POST['username'])
        name = request.POST['username']
        pas = request.POST['password']
        user = User.objects.create_user(username=name, password=pas)
    return render(request, 'header.html')

def logn(request):
    name = request.POST['username']
    pas = request.POST['password']
    user = authenticate(username=name, password=pas)
    if user is not None:
        login(request, user)
    return redirect('/')
