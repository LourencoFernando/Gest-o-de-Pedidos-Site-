from django.shortcuts import render
from .models import BlogClass

# Create your views here.

def Blog(request):
    blog = BlogClass.objects.all()
    return render(request, 'blog.html', {'Blog': blog})