from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Section(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre sección')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

    class Meta:
        verbose_name='sección',
        verbose_name_plural='secciones'
        ordering=['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=100, verbose_name='Título')
    image=models.ImageField(upload_to='product',verbose_name='Imagen')
    price=models.TextField(max_length=50,verbose_name='Precio')
    description=models.TextField(verbose_name='Descripción')
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    section=models.ManyToManyField(Section, verbose_name= 'Sección')
    content=models.TextField(verbose_name='Contenido')
    review=models.TextField(verbose_name='Reviews')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

    class Meta:
        verbose_name='producto',
        verbose_name_plural='productos'
        ordering=['-created']

    def __str__(self):
        return self.title