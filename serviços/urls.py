from django.contrib import admin
from django.urls import path
from .views import Serviços

urlpatterns = [
    path('', Serviços, name='serviços')
]
