from django.contrib import admin
from django.urls import path, re_path, include #nos ayuda a armar las urls
from . import views

app_name = 'producto_app'
 
urlpatterns = [
   path(   #estructura path compuesta por tres partes
       'inicial/',   #asi termina la url (url/lista)
       views.Inicio.as_view(), #esta es la vista que acabamos de crear en views.py	
       name='Pagina inicial'   #nombre de la url
   ),
   path(
    'listaA/',
    views.ProductoListView.as_view(),
    name='Lista de productos'
   ),
   path(
    'buscarA/',
    views.BuscaProductoListView.as_view(),
    name='Buscar producto'
   ),
   path(
    'detalleA/<pk>/',
    views.ProductoDetailView.as_view(),
    name='Detalle del producto'
   ),
   path(
    'createA/',
    views.ProductoCreateView.as_view(),
    name='Alta del producto'
   ),
   path(
    'updateA/<pk>/',
    views.ProductoUpdateView.as_view(),
    name='Modificar producto'
   ),
   path(
    'deleteA/<pk>/',
    views.ProductoDeleteView.as_view(),
    name='Eliminar producto'
   ),
]
#esto se vincula en el archivo principal de urls (persona)
