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
from .models import Proveedor #Importamos el modelo Proveedor
from .forms import ProveedorForm
from django.urls import reverse_lazy

class Inicio(TemplateView):     #Esta vista hereda de TemplateView y solo nos muestra un template
   template_name = "inicio.html" #mostramos el contenido del archivo html llamado inicio.html


class ProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedor/lista.html"
    ordering = 'nombres'
    context_object_name = 'Proveedores'


class BuscaProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedor/buscar.html"
    ordering= 'nombres'
    context_object_name= 'Proveedores'

    def get_queryset(self):
      palabra_clave = self.request.GET.get('kword','')
      lista = Proveedor.objects.filter(
            apellidos__icontains = palabra_clave
      )
      return lista

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = "proveedor/detalle.html"
    context_object_name= 'detalle'


class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = "proveedor/create.html"
    form_class= ProveedorForm
    success_url = reverse_lazy('Proveedor_app:Lista de Proveedores')

    def form_valid(self, form):
        emp = form.save()
        return super(ProveedorCreateView, self).form_valid(form)

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = "proveedor/update.html"
    form_class= ProveedorForm
    success_url = reverse_lazy('Proveedor_app:Lista de Proveedores')

    def form_valid(self, form):
        emp = form.save()
        return super(ProveedorUpdateView, self).form_valid(form)


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = "proveedor/delete.html"
    success_url = reverse_lazy('Proveedor_app:Lista de Proveedores')




   