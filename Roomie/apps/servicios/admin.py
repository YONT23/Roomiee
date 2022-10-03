from django.contrib import admin
from apps.servicios.models import tipo_baño, tipo_formapago, tipo_habitacion, tipo_husped, tipo_pago
from apps.servicios.models import Disponibilidad, Servicio, Pago
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('serv_ubicacion','huesped','habitacion','disponibilidad')


admin.site.register(Disponibilidad)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Pago)
admin.site.register(tipo_baño)
admin.site.register(tipo_habitacion)
admin.site.register(tipo_formapago)
admin.site.register(tipo_husped)
admin.site.register(tipo_pago)