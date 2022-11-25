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
from .models import Empleado #Importamos el modelo empleado
from .forms import EmpleadoForm
from django.urls import reverse_lazy

class Inicio(TemplateView):     #Esta vista hereda de TemplateView y solo nos muestra un template
   template_name = "inicio.html" #mostramos el contenido del archivo html llamado inicio.html


class EmpleadoListView(ListView):
    model = Empleado
    template_name = "empleado/lista.html"
    ordering = 'apellidos'
    context_object_name = 'empleados'


class BuscaEmpleadoListView(ListView):
    model = Empleado
    template_name = "empleado/buscar.html"
    ordering= 'apellidos'
    context_object_name= 'empleados'

    def get_queryset(self):
      palabra_clave = self.request.GET.get('kword','')
      lista = Empleado.objects.filter(
            apellidos__icontains = palabra_clave
      )
      return lista

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detalle.html"
    context_object_name= 'detalle'


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/create.html"
    form_class= EmpleadoForm
    success_url = reverse_lazy('empleado_app:Lista de empleados')

    def form_valid(self, form):
        emp = form.save()
        return super(EmpleadoCreateView, self).form_valid(form)



   