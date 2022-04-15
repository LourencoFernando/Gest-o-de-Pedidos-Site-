from django.contrib import admin
from .models import serviços

# Register your models here.

class serviçosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(serviços, serviçosAdmin)
