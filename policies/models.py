from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre categoría')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

    class Meta:
        verbose_name='categoría',
        verbose_name_plural='categorías'
        ordering=['name']

    def __str__(self):
        return self.name

class Policies(models.Model):
    title=models.CharField(max_length=100, verbose_name='Título')
    published=models.DateTimeField(default=now, verbose_name='Fecha de publicación')
    content=models.TextField(verbose_name='Contenido')
    image=models.ImageField(upload_to='policies',verbose_name='Imagen')
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    category=models.ManyToManyField(Category, verbose_name= 'Categorías')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

    class Meta:
        verbose_name='entrada'
        verbose_name_plural='entradas'
        ordering=['-created']

        def __str__(self):
            return self.title