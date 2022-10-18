from rest_framework import serializers
from apps.servicios.models import *

class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields =('__all__')

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields=('serv_internet','serv_cocina','serv_patio','serv_ubicacion','habitacion','huesped','baño','disponibilidad',)

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pago
        fields=('__all__')
