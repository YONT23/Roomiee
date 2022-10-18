from django.db import models

class TablaMaestra(models.Model):
    tama_nombre1 = models.CharField(max_length=30)
    tama_nombre2 = models.CharField(max_length=30)
    tama_dependencia1 = models.CharField(max_length=30)
    tama_dependencia2 = models.CharField(max_length=30)
    tama_codigo = models.CharField(max_length=30)
    tama_estado = models.CharField(max_length=30)

    def __str__(self):
        return self.tama_nombre1

class Personas(models.Model):
    pers_nombre = models.CharField(max_length=30)
    pers_apellido = models.CharField(max_length=20)
    pers_telefono = models.CharField(max_length=10)
    pers_direccion = models.CharField(max_length=10)
    identificacion = models.ForeignKey(TablaMaestra, null=True, blank=True, on_delete=models.CASCADE)
    pers_numidentidad = models.CharField(max_length=45)

    def __str__(self):
        return self.pers_nombre

class Cliente(models.Model):
    persona = models.ForeignKey(Personas, null=True, blank=True, on_delete=models.CASCADE)
    clie_nacionalidad = models.CharField(max_length=20)
    oficio = models.ForeignKey(TablaMaestra, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.clie_nacionalidad


class Propietario(models.Model):
    prop_respuesta = models.CharField(max_length=60)
    persona = models.ForeignKey(Personas, related_name='Nombre', null=True, blank=True, on_delete=models.CASCADE)
    cliente = models.ManyToManyField(Cliente, through='propietariocliente')

    def __str__(self):
        return self.prop_respuesta

class propietariocliente(models.Model):
    procl_nota = models.CharField(max_length=60)
    propietario = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.procl_nota       

    