"""Roomie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Urls App Personas
    path('personas/', include('apps.personas.urls')),       #Urls Personas
    path('propietarios/', include('apps.personas.urls')),   #Url Propietarios
    path('pxc/', include('apps.personas.urls')),            #Url PropietariosClientes
    path('clientes/', include('apps.personas.urls')),       #Url Clientes
    path('maestra/', include('apps.personas.urls')),        #url tabla maestra
    #Urls App Servicios
    path('servicios/',include('apps.servicios.urls')),      #Url Servicios
    path('pagos/',include('apps.servicios.urls')),          #Url Pagos
    path('disp/',include('apps.servicios.urls'))            #Url Disponibilidad
]
