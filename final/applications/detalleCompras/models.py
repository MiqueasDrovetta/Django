from django.db import models
from applications.productos.models import Producto

# Create your models here.
class DetalleCompra(models.Model):
    """Model definition for DetalleCompras."""

    # TODO: Define fields here
    cantidad = models.IntegerField("Cantidad que compro")    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.FloatField("Precio Unitario")

    class Meta:
        """Meta definition for DetalleCompras."""

        verbose_name = 'DetalleCompra'
        verbose_name_plural = 'DetalleCompras'

    def __str__(self):
        """Unicode representation of DetalleCompras."""
        return f'{self.cantidad}, {self.precio}, {self.producto}'