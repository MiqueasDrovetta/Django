from django.db import models
from applications.detalleCompras.models import DetalleCompra
from applications.proveedores.models import Proveedor

# Create your models here.
class Compra(models.Model):
    """Model definition for Compra."""

    # TODO: Define fields here
    fecha = models.DateField("Fecha de Compra")
    detalle = models.ForeignKey(DetalleCompra, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
  

    class Meta:
        """Meta definition for Compra."""

        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        """Unicode representation of Compra."""
        return f"{self.fecha}"
