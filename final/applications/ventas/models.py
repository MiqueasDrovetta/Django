from django.db import models
from applications.empleado.models import Empleado
from applications.detalleVentas.models import DetalleVenta
from applications.clientes.models import Cliente

# Create your models here.
class Venta(models.Model):
    """Model definition for Venta."""

    # TODO: Define fields here
    fecha = models.DateField("Fecha de venta")
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    detalle = models.ForeignKey(DetalleVenta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  

    class Meta:
        """Meta definition for Venta."""

        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        """Unicode representation of Venta."""
        return f"{self.fecha}, {self.empleado}, {self.detalle}, {self.cliente}"

