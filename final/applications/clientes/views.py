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
from .models import Cliente #Importamos el modelo Cliente
from .forms import ClienteForm
from django.urls import reverse_lazy

class Inicio(TemplateView):     #Esta vista hereda de TemplateView y solo nos muestra un template
   template_name = "inicio.html" #mostramos el contenido del archivo html llamado inicio.html


class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente/lista.html"
    ordering = 'apellidos'
    context_object_name = 'clientes'


class BuscaClienteListView(ListView):
    model = Cliente
    template_name = "cliente/buscar.html"
    ordering= 'apellidos'
    context_object_name= 'clientes'

    def get_queryset(self):
      palabra_clave = self.request.GET.get('kword','')
      lista = Cliente.objects.filter(
            apellidos__icontains = palabra_clave
      )
      return lista

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "cliente/detalle.html"
    context_object_name= 'detalle'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "cliente/create.html"
    form_class= ClienteForm
    success_url = reverse_lazy('cliente_app:Lista de clientes')

    def form_valid(self, form):
        emp = form.save()
        return super(ClienteCreateView, self).form_valid(form)

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "cliente/update.html"
    form_class= ClienteForm
    success_url = reverse_lazy('cliente_app:Lista de clientes')

    def form_valid(self, form):
        emp = form.save()
        return super(ClienteUpdateView, self).form_valid(form)


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "cliente/delete.html"
    success_url = reverse_lazy('cliente_app:Lista de clientes')




   