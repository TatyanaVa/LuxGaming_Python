from django.db import models
from django.utils.timezone import now

# Create your models here.
class Contact (models.Model):
    page= models.CharField(max_length=50, verbose_name="Página")
    greeting=models.TextField(verbose_name="Saludo")
    message=models.TextField(verbose_name="Mensaje")
    ubication=models.TextField(verbose_name="Ubicación")
    phone=models.TextField(verbose_name="Teléfono")
    email=models.TextField(verbose_name="Correo")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="contacto"
        verbose_name="contactos"
        ordering=['-created']
    def __str__(self):
        return self.page
    

