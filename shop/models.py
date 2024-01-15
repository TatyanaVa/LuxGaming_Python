from django.db import models
from django.utils.timezone import now

# Create your models here.
class Shop(models.Model):
    page= models.CharField(max_length=50, verbose_name="Página")
    image=models.ImageField(upload_to='shop',verbose_name='Imagen')
    name=models.CharField(max_length=50, verbose_name='Nombre videojuego')
    precio=models.CharField(max_length=50, verbose_name='Precio')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name='videojuego'
        verbose_name_plural='videojuegos'
        ordering=['-created']

        def __str__(self):
            return self.name