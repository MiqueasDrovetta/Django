from django.db import models
 
# Create your models here.
class Oficina(models.Model):  
   """Campos."""
   
   nombre = models.CharField("Nombre de la Oficina", max_length=50)
   nombre_corto = models.CharField("Nombre corto", max_length=50)
  
   class Meta:
       """Permite agregar informacion al modelo Empleado."""
       verbose_name = 'Oficina'
       verbose_name_plural = 'Oficinas'

   def __str__(self):
        """Unicode representaOficina."""
        return self.nombre_corto
