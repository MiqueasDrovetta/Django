from django.contrib import admin
from .models import Empleado, Puesto #importamos desde models.py el modelo Empleado y Habilidad
 
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Puesto)