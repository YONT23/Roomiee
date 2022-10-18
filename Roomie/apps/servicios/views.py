from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.servicios.models import *
from apps.servicios.serializers import *

##Disponibilidad CRUD

class DisponibilidadView(ListAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

    def get(self, request, *args, **kwargs):
        dispoData = DisponibilidadSerializer(self.get_queryset(), many=True)
        return Response(dispoData.data, status=status.HTTP_200_OK)

class DisponibilidadViewOwner(ListAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

    def get(self, request, *args, **kwargs):
        ServicioData = DisponibilidadSerializer(self.get_queryset(), many=True)
        return Response(ServicioData.data, status=status.HTTP_200_OK)

class DisponibilidadCreate(CreateAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

    def post(self, request, *args, **kwargs):
        createData = DisponibilidadSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class DisponibilidadUpdate(UpdateAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

class DisponibilidadDelete(DestroyAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer


##Servicios CRUD

class ServiciosView(ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def get(self, request, *args, **kwargs):
        servicioData = ServicioSerializer(self.get_queryset(), many=True)
        return Response(servicioData.data, status=status.HTTP_200_OK)

class ServicioViewOwner(ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def get(self, request, *args, **kwargs):
        ServicioData = ServicioSerializer(self.get_queryset(), many=True)
        return Response(ServicioData.data, status=status.HTTP_200_OK)

class ServicioCreate(CreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def post(self, request, *args, **kwargs):
        createData = ServicioSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class ServicioUpdate(UpdateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class ServicioDelete(DestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

##Pago CRUD

class PagoView(ListAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

    def get(self, request, *args, **kwargs):
        pagoData = PagoSerializer(self.get_queryset(), many=True)
        return Response(pagoData.data, status=status.HTTP_200_OK)

class PagoViewOwner(ListAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

    def get(self, request, *args, **kwargs):
        PagoData = PagoSerializer(self.get_queryset(), many=True)
        return Response(PagoData.data, status=status.HTTP_200_OK)

class PagoCreate(CreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

    def post(self, request, *args, **kwargs):
        createData = PagoSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class PagoUpdate(UpdateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoDelete(DestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
