from serviços.admin import serviçosAdmin
from django.shortcuts import render
from .models import serviços

# Create your views here.

def Serviços(request):
    serviçosv = serviços.objects.all()
    return render(request, 'serviços.html', {'Serviços': serviçosv})
