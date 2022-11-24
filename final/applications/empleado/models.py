from django.db import models

# Create your models here.
class Habilidad(models.Model):
    """Model definition for Habilidad."""

    # TODO: Define fields here
    nombre = models.CharField("Nombre de la habilidad", max_length=50)

    class Meta:
        """Meta definition for Habilidad."""

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        """Unicode representation of Habilidad."""
        return f"{self.nombre}"


class Empleado(models.Model):
    """Model definition for Empleado."""

    # TODO: Define fields here

    nombres = models.CharField("Nombres del Empleado", max_length=50)
    apellidos = models.CharField("Apellidos del Empleado", max_length=50)
    dni = models.CharField("DNI", max_length=50)
    habilidades = models.ManyToManyField(Habilidad)
 
    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleado."""
        return f"{self.nombres}, {self.apellidos}"
