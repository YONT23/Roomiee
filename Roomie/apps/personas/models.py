from django.db import models

class tipo_identificacion(models.Model):
    tiid_tipodocumento = models.CharField(max_length=30)
    tiid_numerodocumento = models.CharField(max_length=15)

    def __str__(self):
        return self.tiid_numerodocumento

class Personas(models.Model):
    pers_nombre = models.CharField(max_length=30)
    pers_apellido = models.CharField(max_length=20)
    pers_telefono = models.CharField(max_length=10)
    pers_direccion = models.CharField(max_length=10)
    identificacion = models.ForeignKey(tipo_identificacion, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.pers_nombre

class tipo_oficio(models.Model):
    tiof_oficio = models.CharField(max_length=30)

    def __str__(self):
        return self.tiof_oficio

class Cliente(models.Model):
    persona = models.ForeignKey(Personas, null=True, blank=True, on_delete=models.CASCADE)
    clie_nacionalidad = models.CharField(max_length=20)
    oficio = models.ForeignKey(tipo_oficio, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.clie_nacionalidad


class Propietario(models.Model):
    prop_respuesta = models.CharField(max_length=60)
    persona = models.ForeignKey(Personas, null=True, blank=True, on_delete=models.CASCADE)
    cliente = models.ManyToManyField(Cliente, through='propietariocliente')

    def __str__(self):
        return self.prop_respuesta

class propietariocliente(models.Model):
    procl_nota = models.CharField(max_length=60)
    propietario = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.procl_nota       

    