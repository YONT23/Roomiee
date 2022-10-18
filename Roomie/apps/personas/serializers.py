from rest_framework import serializers
from apps.personas.models import TablaMaestra, Personas, propietariocliente, Propietario, Cliente

class TablaMaestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaMaestra
        fields =('tama_nombre1','tama_nombre2','tama_dependencia1','tama_dependencia2','tama_codigo','tama_estado',)

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personas
        fields=('__all__')

class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Propietario
        fields=('__all__')

class propietarioclienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=propietariocliente
        fields=('__all__')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('clie_nacionalidad','persona','oficio')