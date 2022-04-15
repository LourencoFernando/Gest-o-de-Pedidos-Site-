from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class serviços(models.Model):
    título = models.CharField(max_length=50)
    conteúdo = models.CharField(max_length=1000)
    imagem = models.ImageField(upload_to='Serviços')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    

    def __str__(self):
        return self.título
