from django.db import models

# Create your models here.
class Puesto(models.Model):
    """Model definition for Puesto."""

    # TODO: Define fields here
    nombre = models.CharField("Nombre del Puesto", max_length=50)

    class Meta:
        """Meta definition for Puesto."""

        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'

    def __str__(self):
        """Unicode representation of Puesto."""
        return self.nombre


class Empleado(models.Model):
    """Model definition for Empleado."""

    # TODO: Define fields here

    nombres = models.CharField("Nombres del Empleado", max_length=50)
    apellidos = models.CharField("Apellidos del Empleado", max_length=50)
    dni = models.CharField("DNI", max_length=50)
    puesto = models.ManyToManyField(Puesto)
 
    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleado."""
        return f"{self.puesto}: {self.nombres}, {self.apellidos}"
