from django.contrib import admin
from django.urls import path, re_path, include #nos ayuda a armar las urls
from . import views

app_name = 'empleado_app'
 
urlpatterns = [
   path(   #estructura path compuesta por tres partes
       'inicial/',   #asi termina la url (url/lista)
       views.Inicio.as_view(), #esta es la vista que acabamos de crear en views.py	
       name='Pagina inicial'   #nombre de la url
   ),
   path(
    'lista/',
    views.EmpleadoListView.as_view(),
    name='Lista de empleados'
   ),
   path(
    'buscar/',
    views.BuscaEmpleadoListView.as_view(),
    name='Buscar empleado'
   ),
   path(
    'detalle/<pk>/',
    views.EmpleadoDetailView.as_view(),
    name='Detalle del empleado'
   ),
   path(
    'create/',
    views.EmpleadoCreateView.as_view(),
    name='Alta del empleado'
   ),
]
#esto se vincula en el archivo principal de urls (persona)
