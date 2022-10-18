from django.urls import path
from .views import *

urlpatterns = [
    #Url Personas
    path('', PersonasView.as_view()),
    path('create/', PersonasCreate.as_view()),
    path('update/<int:pk>/', PersonasUpdate.as_view()),
    path('delete/<int:pk>/', PersonasDelete.as_view()),
    path('all/', PersonasViewOwner.as_view()),

    #Url TablaMaestra
    path('m', TablaMaestraView.as_view()),
    path('mcreate/', TablaMaestraCreate.as_view()),
    path('mupdate/<int:pk>/', TablaMaestraUpdate.as_view()),
    path('mdelete/<int:pk>/', TablaMaestraDelete.as_view()),
    path('mall/', TablaMaestraViewOwner.as_view()),

    #Urls Clientes
    path('c', ClienteView.as_view()),
    path('ccreate/', ClienteCreate.as_view()),
    path('cupdate/<int:pk>/', ClienteUpdate.as_view()),
    path('cdelete/<int:pk>/', ClienteDelete.as_view()),
    path('call/', ClienteViewOwner.as_view()),

    #Urls Propietario
    path('pp', PropietarioView.as_view()),
    path('ppcreate/', PropietarioCreate.as_view()),
    path('ppupdate/<int:pk>/', PropietarioUpdate.as_view()),
    path('ppdelete/<int:pk>/', PropietarioDelete.as_view()),
    path('ppall/', PropietarioViewOwner.as_view()),

    #Urls propietariocliente
    path('pc', propietarioclienteView.as_view()),
    path('pccreate/', propietarioclienteCreate.as_view()),
    path('pcupdate/<int:pk>/', propietarioclienteUpdate.as_view()),
    path('pcdelete/<int:pk>/', propietarioclienteDelete.as_view()),
    path('pcall/', propietarioclienteViewOwner.as_view()),
]