from django.contrib import admin
from django.urls import path
from .views import Blog

urlpatterns = [
    path('', Blog, name='blog')
]
