from django.contrib import admin
from .models import Producto, Marca, Categoria, Unidad

# Register your models here.
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Unidad)