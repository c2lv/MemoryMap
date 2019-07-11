from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import LoginForm

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
            return render(request, 'signup.html', {'error' : 'Passwords must match'}
            )
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        # form에 정보를 넘겨 저장
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = auth.authenticate(username=username, password=password)
        # user가 none인 경우 인증 정보가 없다.
        if user is not None:
            auth.login(request, user) # user로 login 시도
            return redirect('home')
        else:
            return HttpResponse("다시 시도")
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})