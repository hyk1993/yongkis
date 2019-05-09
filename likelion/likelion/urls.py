from django.contrib import admin
from django.urls import path
from comment import views

app_name = 'comment'
urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('', views.blog, name='blog'),
    path('newblog/', views.blogpost, name="newblog"),
    path('newcomment/<int:blog_id>/', views.newcomment, name="newcomment"),
]