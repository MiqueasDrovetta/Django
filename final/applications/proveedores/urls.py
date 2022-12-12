from django.contrib import admin
from django.urls import path, re_path, include #nos ayuda a armar las urls
from . import views

app_name = 'Proveedor_app'
 
urlpatterns = [
   path(   #estructura path compuesta por tres partes
       'inicial/',   #asi termina la url (url/lista)
       views.Inicio.as_view(), #esta es la vista que acabamos de crear en views.py	
       name='Pagina inicial'   #nombre de la url
   ),
   path(
    'listaP/',
    views.ProveedorListView.as_view(),
    name='Lista de Proveedores'
   ),
   path(
    'buscarP/',
    views.BuscaProveedorListView.as_view(),
    name='Buscar Proveedor'
   ),
   path(
    'detalleP/<pk>/',
    views.ProveedorDetailView.as_view(),
    name='Detalle del Proveedor'
   ),
   path(
    'createP/',
    views.ProveedorCreateView.as_view(),
    name='Alta del Proveedor'
   ),
   path(
    'updateP/<pk>/',
    views.ProveedorUpdateView.as_view(),
    name='Modificar Proveedor'
   ),
   path(
    'deleteP/<pk>/',
    views.ProveedorDeleteView.as_view(),
    name='Eliminar Proveedor'
   ),
]
#esto se vincula en el archivo principal de urls (persona)
