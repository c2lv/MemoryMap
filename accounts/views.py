from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        #새 계정 생성
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"]
                )
            user.save()
            auth.login(request,user)
            return redirect('blogHome')
        else:
            return render(request, 'accounts/signup.html', {'error' : 'Passwords must match'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blogHome')
    return render(request, 'accounts/signup.html')