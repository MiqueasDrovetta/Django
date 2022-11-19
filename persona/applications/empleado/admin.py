from django.contrib import admin

# Register your models here.
from.models import Empleado #importamos desde models.py el modelo Empleado y Habilidad
 
# Register your models here.
admin.site.register(Empleado)
