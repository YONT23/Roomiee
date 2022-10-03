from django.db import models


class Disponibilidad(models.Model):
    disp_disponible = models.CharField(max_length=2)
    disp_precio = models.BigIntegerField()
    
    def __str__(self):
        return self.disp_disponible

class tipo_habitacion(models.Model):
    tiha_cuantas = models.CharField(max_length=3)

    def __str__(self):
        return self.tiha_cuantas

class tipo_baño(models.Model):
    tiba_cuantos = models.CharField(max_length=3)

    def __str__(self):
        return self.tiba_cuantos

class tipo_husped(models.Model):
    tihu_cuantos = models.CharField(max_length=3)

    def __str__(self):
        return self.tihu_cuantos

class Servicio(models.Model):
    serv_internet = models.CharField(max_length=2)
    serv_cocina = models.CharField(max_length=3)
    serv_patio = models.CharField(max_length=3)
    serv_ubicacion = models.CharField(max_length=30)
    habitacion = models.ForeignKey(tipo_habitacion, null=True, blank=True, on_delete=models.CASCADE)
    huesped = models.ForeignKey(tipo_husped, null=True, blank=True, on_delete=models.CASCADE)
    baño = models.ForeignKey(tipo_baño, null=True, blank=True, on_delete=models.CASCADE)
    disponibilidad = models.ForeignKey(Disponibilidad, null=True, blank=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.serv_ubicacion

class tipo_pago(models.Model):
    tipa_pago = models.CharField(max_length=20)

    def __str__(self):
        return self.tipa_pago

class tipo_formapago(models.Model):
    tifo_forma = models.CharField(max_length=20)

    def __str__(self):
        return self.tifo_forma

class Pago(models.Model):
    realizado = models.CharField(max_length=20)
    pago_fechae = models.DateField()
    pago_fechas = models.DateField()
    pago_valor = models.BigIntegerField()
    servicio = models.ForeignKey(Servicio, null=True, blank=True, on_delete=models.CASCADE)
    tipopago = models.ForeignKey(tipo_pago, null=True, blank=True, on_delete=models.CASCADE)
    formapago = models.ForeignKey(tipo_formapago, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.realizado

