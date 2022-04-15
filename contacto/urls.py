from django.contrib import admin
from django.urls import path
from .views import contactosForm

urlpatterns = [
    path('', contactosForm, name='contacto')
]
