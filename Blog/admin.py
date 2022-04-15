from django.contrib import admin
from .models import BlogClass

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(BlogClass, BlogAdmin)
