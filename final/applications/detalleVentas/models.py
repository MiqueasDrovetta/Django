from django.db import models
from applications.productos.models import Producto

# Create your models here.
class DetalleVenta(models.Model):
    """Model definition for DetalleVenta."""

    # TODO: Define fields here
    cantidad = models.IntegerField("Cantidad que lleva")    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.FloatField("Precio Unitario")

    class Meta:
        """Meta definition for DetalleVenta."""

        verbose_name = 'DetalleVenta'
        verbose_name_plural = 'DetalleVentas'

    def __str__(self):
        """Unicode representation of DetalleVenta."""
        return f'{self.cantidad}, {self.precio}, {self.producto}'

