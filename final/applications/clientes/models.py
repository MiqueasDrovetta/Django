from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Model definition for Cliente."""
    nombres = models.CharField("Nombres del Cliente", max_length=50)
    apellidos = models.CharField("Apellidos del Cliente", max_length=50)
    dni = models.CharField("DNI", max_length=50)
    direccion = models.CharField("Direccion", max_length=50)
    telefono = models.CharField("Telefono", max_length=50)
    fecha = models.DateField("Fecha de alta")

    # TODO: Define fields here

    class Meta:
        """Meta definition for Cliente."""


        verbose_name = 'Cliente'

        verbose_name_plural = 'Clientes'


    def __str__(self):
        """Unicode representation of Cliente."""
        return f"{self.nombres}, {self.apellidos}"

