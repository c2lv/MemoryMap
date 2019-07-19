from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogHome, name="home"),
    path('<username>/new_post/', views.new_post, name="new_post"),
    path('<username>/update_post/<int:id>', views.update_post, name="update_post"),
    path('<username>/delete_post/<int:id>', views.delete_post, name="delete_post"),

    path('<username>/new_memo/<int:id>', views.new_memo, name="new_memo"),
    path('<username>/update_memo/<int:id>', views.update_memo, name="update_memo"),
    path('<username>/delete_memo/<int:id>', views.delete_memo, name="delete_memo"),

    # path('<username>/', views.my_page, name="myPage"),
    # path('<username>/profile', views.profile, name="profile"),
    # path('<username>/<int:id>', views.detail, name="detail"),
    # path('new/', views.new_data, name="new"),
    
]
