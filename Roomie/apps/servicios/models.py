from unicodedata import name
from django.db import models

from apps.personas.models import TablaMaestra


class Disponibilidad(models.Model):
    disp_disponible = models.CharField(max_length=2)
    disp_precio = models.BigIntegerField()
    
    def __str__(self):
        return self.disp_disponible

class Servicio(models.Model):
    serv_internet = models.CharField(max_length=2)
    serv_cocina = models.CharField(max_length=3)
    serv_patio = models.CharField(max_length=3)
    serv_ubicacion = models.CharField(max_length=30)
    habitacion = models.ForeignKey(TablaMaestra, related_name='habitacion', null=True, blank=True, on_delete=models.CASCADE)
    huesped = models.ForeignKey(TablaMaestra, related_name='huesped', null=True, blank=True, on_delete=models.CASCADE)
    baño = models.ForeignKey(TablaMaestra, related_name='baño', null=True, blank=True, on_delete=models.CASCADE)
    disponibilidad = models.ForeignKey(Disponibilidad, related_name='dispo', null=True, blank=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.serv_ubicacion

class Pago(models.Model):
    realizado = models.CharField(max_length=20)
    pago_fechae = models.DateField()
    pago_fechas = models.DateField()
    pago_valor = models.BigIntegerField()
    servicio = models.ForeignKey(Servicio, null=True, blank=True, on_delete=models.CASCADE)
    tipopago = models.ForeignKey(TablaMaestra, related_name='tipopago', null=True, blank=True, on_delete=models.CASCADE)
    formapago = models.ForeignKey(TablaMaestra, related_name='formapago', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.realizado

