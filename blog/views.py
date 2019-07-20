from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Mapmodel, Memo
from .forms import *

from django.http import HttpResponse

from utils.decorators import login_required

# Create your views here.
def main(request):
    return render(request, 'main.html')


def blogHome(request):
    posts = Mapmodel.objects
    form = MemoForm()
    return render(request, 'blogHome.html', {'posts':posts, 'form':form})


def myBlog(request, username):
    posts = Mapmodel.objects.filter(owner=request.user)
    form = MemoForm()
    return render(request, 'myBlog.html', {'posts':posts, 'form':form})


def new_post(request, username):
    if request.method == "POST":
        form = MapForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect("blog:home")
    else:
        form = MapForm()
    return render(request, 'save_data.html', {'form':form})


def update_post(request, username, id):
    post = get_object_or_404(Mapmodel, pk=id)
    form = MapForm(request.POST, instance=post)
    if request.method == "POST":
        form = MapForm(request.POST, instance=post)
        if form.is_valid():
            print(form.cleaned_data)
            post = form.save(commit=False)
            post.save()
            return redirect('blog:home')
    else:
        form = MapForm(instance=post)
    return render(request, 'save_data.html', {'form':form, 'post':post})


def delete_post(request, username, id):
    post = get_object_or_404(Mapmodel, pk=id)
    post.delete()
    return redirect("blog:home")


def new_memo(request, username, id):
    post = get_object_or_404(Mapmodel, pk=id)
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.owner = request.user
            memo.target = post
            memo.save() 
            # return HttpResponse(memo.memo)
        return redirect("blog:home")


def update_memo(request, username, id):
    memo = get_object_or_404(Memo, pk=id)
    form = MapForm(request.POST, instance=memo)
    return render(request, 'save_data.html', {'form':form})

def delete_memo(request, username, id):
    memo = get_object_or_404(Memo, pk=id)
    memo.delete()
    return redirect("blog:home")

#좋아요 기능
@login_required
def like_toggle(request, writer, id):
    # GET파라미터로 전달된 이동할 URL
    next_path = request.GET.get('next')
    # post_pk에 해당하는 Post객체
    post = get_object_or_404(Mapmodel, pk=id)
    # 요청한 사용자
    user = request.user

    target = user.likes.filter(pk=post.id)
    
    # 이미 likes에 존재할 시 삭제, 없을 시 추가
    if target.exists():
        user.likes.remove(post)
    else:
        user.likes.add(post)

    # next 기능을 사용할 시 활성화
    # if next_path:
    #     return redirect(next_path)
    return redirect('blog:home')

# def save_data(request, id):
#     data, created = Mapmodel.objects.get_or_create(pk=id)
#     form = MapForm(request.POST, instance=data)

#     # 데이터가 이미 존재 할 때 Update
#     if form.is_valid():
#         form.save()
#         return redirect(data.get_absolute_url())
#     # 데이터가 존재하지 않을 때 Create
#     else:
#         return render('save_data.html', {'form':form})

