from django.urls import path
from .views import *

urlpatterns = [
    path('', ServiciosView.as_view()),
    path('create/', ServicioCreate.as_view()),
    path('update/<int:pk>/', ServicioUpdate.as_view()),
    path('delete/<int:pk>/', ServicioDelete.as_view()),
    path('all/', ServicioViewOwner.as_view()),

    #Urls Pagos
    path('p', PagoView.as_view()),
    path('pcreate/', PagoCreate.as_view()),
    path('pupdate/<int:pk>/', PagoUpdate.as_view()),
    path('pdelete/<int:pk>/', PagoDelete.as_view()),
    path('pall/', PagoViewOwner.as_view()),

    #Urls Disponibles
    path('d', DisponibilidadView.as_view()),
    path('dcreate/', PagoCreate.as_view()),
    path('dupdate/<int:pk>/', PagoUpdate.as_view()),
    path('ddelete/<int:pk>/', PagoDelete.as_view()),
    path('dall/', DisponibilidadViewOwner.as_view()),
]

