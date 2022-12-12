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
from .models import Producto #Importamos el modelo Producto
from .forms import ProductoForm
from django.urls import reverse_lazy

class Inicio(TemplateView):     #Esta vista hereda de TemplateView y solo nos muestra un template
   template_name = "inicio.html" #mostramos el contenido del archivo html llamado inicio.html


class ProductoListView(ListView):
    model = Producto
    template_name = "producto/lista.html"
    ordering = 'nombre'
    context_object_name = 'productos'


class BuscaProductoListView(ListView):
    model = Producto
    template_name = "producto/buscar.html"
    ordering= 'nombre'
    context_object_name= 'productos'

    def get_queryset(self):
      palabra_clave = self.request.GET.get('kword','')
      lista = Producto.objects.filter(
            apellidos__icontains = palabra_clave
      )
      return lista

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "producto/detalle.html"
    context_object_name= 'detalle'


class ProductoCreateView(CreateView):
    model = Producto
    template_name = "producto/create.html"
    form_class= ProductoForm
    success_url = reverse_lazy('producto_app:Lista de productos')

    def form_valid(self, form):
        emp = form.save()
        return super(ProductoCreateView, self).form_valid(form)

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "producto/update.html"
    form_class= ProductoForm
    success_url = reverse_lazy('producto_app:Lista de productos')

    def form_valid(self, form):
        emp = form.save()
        return super(ProductoUpdateView, self).form_valid(form)


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "producto/delete.html"
    success_url = reverse_lazy('producto_app:Lista de productos')




   