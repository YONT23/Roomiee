from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.models import TblInmueble, TblAlquiler
from ..serializers import inmuebleSerializer, alquilerSerializer
from django.db.models import Count
from django.shortcuts import render, redirect


class Consulta1(ListAPIView):
    queryset = TblAlquiler.objects.all()
    serializer_class = alquilerSerializer

    def consulta1(request):
        fecha1 = request.POST.get('fecha1')
        fecha2 = request.POST.get('fecha2')

        contexto = {
            'fecha1': fecha1,
            'fecha2': fecha2,
        }

    def get_queryset(self):
        return TblAlquiler.objects.values('usuario_id', 'precio', 'fecha_inicio', 'fecha_final').filter(fecha_inicio__range=[fecha1, fecha2])

    def get(self, request, *args, **kwargs):
        consulta1 = alquilerSerializer(self.get_queryset(), many=True)
        return Response(consulta1.data, status=status.HTTP_200_OK)


"""        def post(self, request, *args, **kwargs):
        print(request.data)
        inmueble = request.data
        inmueble['dueño'] = request.user.id
        inmueble['pais_id'] = request.data['pais']
        createData = inmuebleSerializer(data=inmueble)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)"""

    #Consulta2 = TblAlquiler.objects.select_related('usuario_id__username').only('precio', 'fecha_inicio', 'fecha_final')[:10]

