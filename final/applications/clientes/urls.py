from django.contrib import admin
from django.urls import path, re_path, include #nos ayuda a armar las urls
from . import views

app_name = 'cliente_app'
 
urlpatterns = [
   path(   #estructura path compuesta por tres partes
       'inicial/',   #asi termina la url (url/lista)
       views.Inicio.as_view(), #esta es la vista que acabamos de crear en views.py	
       name='Pagina inicial'   #nombre de la url
   ),
   path(
    'listaC/',
    views.ClienteListView.as_view(),
    name='Lista de clientes'
   ),
   path(
    'buscarC/',
    views.BuscaClienteListView.as_view(),
    name='Buscar clientes'
   ),
   path(
    'detalleC/<pk>/',
    views.ClienteDetailView.as_view(),
    name='Detalle del cliente'
   ),
   path(
    'createC/',
    views.ClienteCreateView.as_view(),
    name='Alta del cliente'
   ),
   path(
    'updateC/<pk>/',
    views.ClienteUpdateView.as_view(),
    name='Modificar cliente'
   ),
   path(
    'deleteC/<pk>/',
    views.ClienteDeleteView.as_view(),
    name='Eliminar cliente'
   ),
]
#esto se vincula en el archivo principal de urls (persona)
