from django.db import models

# Create your models here.

class BlogClass(models.Model):
    tema = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    data = models.DateField()
    conteudo = models.CharField(max_length=400)
    imagem = models.ImageField(upload_to='Blog')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
    

    def __str__(self):
        return self.tema
