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
    posts = Mapmodel.objects.all()
    form = MemoForm()
    return render(request, 'blogHome.html', {'posts':posts, 'form':form})


@login_required
def myBlog(request):
    posts = Mapmodel.objects.filter(owner=request.user)
    form = MemoForm()
    return render(request, 'myBlog.html', {'posts':posts, 'form':form})


@login_required
def new_post(request, username):
    if request.method == "POST":
        form = MapForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            tags = form.cleaned_data['tags']
            post = form.save(commit=False)
            post.owner = request.user
            post.save()

            for tag in tags:
               post.tags.add(tag)
               
            return redirect("blog:home")
    else:
        form = MapForm()
    return render(request, 'save_data.html', {'form':form})



def update_post(request, username, id):
    post = get_object_or_404(Mapmodel, pk=id)
    # 글의 주인이 아닐 때
    if post.owner != request.user:
        return redirect('blog:home')
    form = MapForm(request.POST, instance=post)
    if request.method == "POST":
        form = MapForm(request.POST, instance=post)
        if form.is_valid():
            print(form.cleaned_data)
            tags = form.cleaned_data['tags']
            post = form.save(commit=False)
            post.save()

            for tag in tags:
               post.tags.add(tag)
            
            return redirect('blog:home')
    else:
        form = MapForm(instance=post)
    return render(request, 'save_data.html', {'form':form, 'post':post})


def delete_post(request, username, id):
    if request.method == "POST":
        print("삭제합니다.")
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
    if request.method == "POST":        
        memo = get_object_or_404(Memo, pk=id)
        if memo.owner == request.user:
            form = MapForm(request.POST, instance=memo)
            return render(request, 'save_data.html', {'form':form})


def delete_memo(request, username, id):
    if request.method == "POST":
        memo = get_object_or_404(Memo, pk=id)
        if memo.owner == request.user:
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


def search(request):
    # tag = request.POST['q']
    tag = request.GET['target']
    posts = Mapmodel.objects.filter(tags__name__in=[tag])
    form = MemoForm()
    return render(request, "search.html", {"posts":posts, "form":form})