from django.contrib import admin
from apps.personas.models import Personas, propietariocliente, Propietario, Cliente, TablaMaestra
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pers_nombre','pers_apellido','pers_telefono','identificacion')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('persona','clie_nacionalidad','oficio')

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('prop_respuesta','persona')

class propietarioclienteAdmin(admin.ModelAdmin):
    list_display = ('procl_nota','cliente_id')

class TablaMaestraAdmin(admin.ModelAdmin):
    list_display = ('tama_nombre1','tama_nombre2','tama_dependencia1','tama_dependencia2','tama_codigo','tama_estado',)



admin.site.register(Personas,PersonaAdmin)
admin.site.register(Propietario,PropietarioAdmin)
admin.site.register(propietariocliente,propietarioclienteAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(TablaMaestra,TablaMaestraAdmin)
