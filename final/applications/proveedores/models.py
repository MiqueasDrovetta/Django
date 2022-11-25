from django.db import models

# Create your models here.
class Proveedor(models.Model):
    """Model definition for Proveedor."""

    # TODO: Define fields here
    nombres = models.CharField("Razon Social o \n nombre de empresa", max_length=50)
    representante = models.CharField("Nombre completo del representante", max_length=50)
    cuit = models.CharField("CUIT de la empresa", max_length=50)
    direccion = models.CharField("Direccion de la empresa", max_length=50)
    telefono = models.CharField("Telefono de la empresa", max_length=50)
    email = models.CharField("Email de la empresa", max_length=50)
    fecha = models.DateField("Fecha de alta")
    

    class Meta:
        """Meta definition for Proveedor."""

        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        """Unicode representation of Proveedor."""
        return f"{self.nombres}, {self.direccion}"

