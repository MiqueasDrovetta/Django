from django.db import models

# Create your models here.
class Oficina(models.Model):
    """Model definitOficina."""
    nombre = models.CharField("Nombre de la Oficina", max_length=50)
    nombre_corto = models.CharField("Nombre corto", max_length=50)


    # TODO: Define fields here

    class Meta:
        """Meta definitOficina."""

        verbose_name ='Oficina'
        verbose_name_prural='Oficinas'

    def __str__(self):
        """Unicode representaOficina."""
        return self.nombre_corto
