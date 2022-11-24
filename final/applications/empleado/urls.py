from django.contrib import admin
from django.urls import path, re_path, include #nos ayuda a armar las urls
from . import views
 
urlpatterns = [
   path(   #estructura path compuesta por tres partes
       'lista/',   #asi termina la url (url/lista)
       views.Inicio.as_view(), #esta es la vista que acabamos de crear en views.py	
       name='Pagina inicial'   #nombre de la url
   )
]
#esto se vincula en el archivo principal de urls (persona)
