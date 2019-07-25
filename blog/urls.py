from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.blogHome, name="home"),
    # blog post
    path('myblog/', views.myBlog, name="my_blog"),
    path('<username>/new_post/', views.new_post, name="new_post"),
    path('<username>/update_post/<int:id>', views.update_post, name="update_post"),
    path('<username>/delete_post/<int:id>', views.delete_post, name="delete_post"),

    path('<str:writer>/<int:id>/like-toggle', views.like_toggle, name="post_like_toggle"),

    # blog comment, memo
    path('<username>/new_memo/<int:id>', views.new_memo, name="new_memo"),
    path('<username>/update_memo/<int:id>', views.update_memo, name="update_memo"),
    path('<username>/delete_memo/<int:id>', views.delete_memo, name="delete_memo"),
    
    path('search/', views.search, name="search")
]
