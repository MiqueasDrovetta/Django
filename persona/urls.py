"""persona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import pathpath, re_path, include #nos ayuda a armar las urls


urlpatterns = [
    path(   #estructura path compuesta por tres partes
       'lista/',   #asi termina la url (url/lista)
       views.Inicio.as_view(), #esta es la vista que acabamos de crear en views.py
       name='Pagina inicial'   #nombre de la url
   )
]
#esto se vincula en el archivo principal de urls (persona)
