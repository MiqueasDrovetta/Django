from django.db import models

# Create your models here.
class Empleado(models.Model):
    """Model definition for Empleado."""

    # TODO: Define fields here

    nombres = models.CharField("Nombres del Empleado", max_length=50)
    apellidos = models.CharField("Apellidos del Empleado", max_length=50)
    dni = models.CharField("DNI", max_length=50)
    # area = models.ForeignKey(Oficina, on_delete=models.CASCADE) 
 
    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleado."""
        return f"{self.nombres} {self.apellidos}"
