from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.personas.models import *
from apps.personas.serializers import *

##Tabla Maestra CRUD
class TablaMaestraView(ListAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer

    def get(self, request, *args, **kwargs):
        maestraData = TablaMaestraSerializer(self.get_queryset(), many=True)
        return Response(maestraData.data, status=status.HTTP_200_OK)

class TablaMaestraViewOwner(ListAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer

    def get(self, request, *args, **kwargs):
        ServicioData = TablaMaestraSerializer(self.get_queryset(), many=True)
        return Response(ServicioData.data, status=status.HTTP_200_OK)

class TablaMaestraCreate(CreateAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer

    def post(self, request, *args, **kwargs):
        createData = TablaMaestraSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class TablaMaestraUpdate(UpdateAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer

class TablaMaestraDelete(DestroyAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer


##Personas CRUD

class PersonasView(ListAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

    def get(self, request, *args, **kwargs):
        personaData = PersonasSerializer(self.get_queryset(), many=True)
        return Response(personaData.data, status=status.HTTP_200_OK)

class PersonasViewOwner(ListAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

    def get(self, request, *args, **kwargs):
        personaData = PersonasSerializer(self.get_queryset(), many=True)
        return Response(personaData.data, status=status.HTTP_200_OK)

class PersonasCreate(CreateAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

    def post(self, request, *args, **kwargs):
        createData = PersonasSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonasUpdate(UpdateAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer


class PersonasDelete(DestroyAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

##Cliente CRUD

class ClienteView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        clienteData = ClienteSerializer(self.get_queryset(), many=True)
        return Response(clienteData.data, status=status.HTTP_200_OK)

class ClienteViewOwner(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        clienteData = ClienteSerializer(self.get_queryset(), many=True)
        return Response(clienteData.data, status=status.HTTP_200_OK)

class ClienteCreate(CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def post(self, request, *args, **kwargs):
        createData = ClienteSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteUpdate(UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDelete(DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

##Propietario CRUD

class PropietarioView(ListAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

    def get(self, request, *args, **kwargs):
        propietarioData = PropietarioSerializer(self.get_queryset(), many=True)
        return Response(propietarioData.data, status=status.HTTP_200_OK)

class PropietarioViewOwner(ListAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

    def get(self, request, *args, **kwargs):
        propietarioData = PropietarioSerializer(self.get_queryset(), many=True)
        return Response(propietarioData.data, status=status.HTTP_200_OK)

class PropietarioCreate(CreateAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

    def post(self, request, *args, **kwargs):
        createData = PropietarioSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class PropietarioUpdate(UpdateAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

class PropietarioDelete(DestroyAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

##propietariocliente CRUD

class propietarioclienteView(ListAPIView):
    queryset = propietariocliente.objects.all()
    serializer_class = propietarioclienteSerializer

    def get(self, request, *args, **kwargs):
        propietarioclienteData = propietarioclienteSerializer(self.get_queryset(), many=True)
        return Response(propietarioclienteData.data, status=status.HTTP_200_OK)

class propietarioclienteViewOwner(ListAPIView):
    queryset = propietariocliente.objects.all()
    serializer_class = propietarioclienteSerializer

    def get(self, request, *args, **kwargs):
        propietarioclienteData = propietarioclienteSerializer(self.get_queryset(), many=True)
        return Response(propietarioclienteData.data, status=status.HTTP_200_OK)

class propietarioclienteCreate(CreateAPIView):
    queryset = propietariocliente.objects.all()
    serializer_class = propietarioclienteSerializer

    def post(self, request, *args, **kwargs):
        createData = propietarioclienteSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class propietarioclienteUpdate(UpdateAPIView):
    queryset = propietariocliente.objects.all()
    serializer_class = propietarioclienteSerializer

class propietarioclienteDelete(DestroyAPIView):
    queryset = propietariocliente.objects.all()
    serializer_class = propietarioclienteSerializer
