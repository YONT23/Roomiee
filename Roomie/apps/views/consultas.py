from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
import json
import json as simplejson
from rest_framework.response import Response
from ..servicios.models import *
from django.db.models.functions import Lower

class Consulta1(APIView):

    def get(self, resquest, *args, **kwargs):
        clientes = TblPersona.objects.all().values()
        mujeres = TblPersona.objects.filter(tipo_sexo=3).values()
        hombres = TblPersona.objects.filter(tipo_sexo=2).values()

        response = {
            "clientes_totales": len(clientes),
            "clientes_mujeres": len(mujeres),
            "clientes_hombres": len(hombres)
        }

        return JsonResponse(response, safe=False)

class Consulta2(APIView):

    def get(self, resquest, *args, **kwargs):
        fecha1 = resquest.POST.get('fecha1')
        fecha2 = resquest.POST.get('fecha2')

        consulta = TblAlquiler.objects.values('precio','fecha_inicio','fecha_final','usuario_id__username').filter(fecha_inicio__range=[fecha1,fecha2])

        response = {
            "fecha1": fecha1,
            "fecha2": fecha2,
            "consulta": consulta
        }

        return HttpResponse({response, list(consulta)})

class Consulta3(APIView):

    def get(self, resquest, *args, **kwargs):
        result_list = list(TblPago.objects.values('pago_fecha', 'pago_valor'))

        return HttpResponse(json.dumps(result_list))

class Consulta4(APIView):

    def get(self, resquest, *args, **kwargs):
        q = TblPago.objects.filter(tipo_pago__maes_nombre='Efectivo')

        return HttpResponse(json.dumps(q))