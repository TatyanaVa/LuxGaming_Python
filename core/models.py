from django.db import models

# Create your models here.
class Product(models.Model):
    page= models.CharField(max_length=100, verbose_name="Página")
    product=models.CharField(max_length=100, verbose_name="Producto")
    subtitle=models.TextField(verbose_name="Subtítulo")
    precio=models.TextField(verbose_name="Precio")
    image=models.ImageField(upload_to="product",verbose_name="Imagen")
    identific=models.CharField(max_length=10,verbose_name="Identificación")
    category=models.CharField(max_length=100,verbose_name="Categoría")
    platform=models.CharField(max_length=100,verbose_name="Plataforma")
    desciption=models.TextField(verbose_name="Descripción")
    review=models.TextField(verbose_name="Reviews")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="product"
        verbose_name_plural="productos"
        ordering=['-created']

    def  __str__(self):
        return self.product
    