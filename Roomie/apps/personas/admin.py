from django.contrib import admin
from apps.personas.models import Personas, propietariocliente, Propietario, Cliente, tipo_identificacion,tipo_oficio
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pers_nombre','pers_apellido','pers_telefono','identificacion')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('persona','clie_nacionalidad','oficio')

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('prop_respuesta','persona')

class propietarioclienteAdmin(admin.ModelAdmin):
    list_display = ('procl_nota','cliente_id')

class tipo_identificacionAdmin(admin.ModelAdmin):
    list_display = ('tiid_tipodocumento','tiid_numerodocumento')



admin.site.register(Personas,PersonaAdmin)
admin.site.register(Propietario,PropietarioAdmin)
admin.site.register(propietariocliente,propietarioclienteAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(tipo_identificacion, tipo_identificacionAdmin)
admin.site.register(tipo_oficio)