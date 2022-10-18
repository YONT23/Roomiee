from django.contrib import admin
from apps.servicios.models import Disponibilidad, Servicio, Pago
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('serv_ubicacion','huesped','habitacion','disponibilidad')


admin.site.register(Disponibilidad)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Pago)
