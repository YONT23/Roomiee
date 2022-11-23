from django.urls import path
from ..views.inmuebles import *
from ..views.consultas import Consulta1

urlpatterns = [
    path('', InmuebleView.as_view()),
    path('create/', InmuebleCreate.as_view()),
    path('update/<int:pk>/', InmuebleUpdate.as_view()),
    path('delete/<int:pk>/', InmuebleDelete.as_view()),
    path('all/', InmuebleViewOwner.as_view()),
    path('consulta1/', Consulta1.as_view()),
]