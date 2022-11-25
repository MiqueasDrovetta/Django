from django.contrib import admin
from .models import Cliente #importamos desde models.py el modelo Empleado y Habilidad
 
# Register your models here.
admin.site.register(Cliente)
