from django.shortcuts import render
 
# Create your views here.
from django.views.generic import (  #importamos las vistas basadas en clases
   ListView,   #Cuando se hace una consulta devuelve una lista del registro de la base de datos
   DetailView, #Obtenemos los detalles de un registro de la base de datos
   CreateView, #Damos de alta un registro en la base de datos
   TemplateView,   #Para mostrar un template
   UpdateView, #nos ayuda a actualizar o editar un registro de la base de datos
   DeleteView #nos permite borrar un registro de la base de datos
)
 
#Creacion de vista inicial
from .models import Proveedor #Importamos el modelo proveedor

class Inicio(TemplateView):     #Esta vista hereda de TemplateView y solo nos muestra un template
   template_name = "inicio.html" #mostramos el contenido del archivo html llamado inicio.html
