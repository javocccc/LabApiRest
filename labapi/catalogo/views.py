from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cancion, Libro
from .serializers import CancionSerializer, LibroSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('id')
    serializer_class = LibroSerializer


class CancionList(APIView):
    def get(self, request):
        canciones = Cancion.objects.all().order_by('id')
        serializer = CancionSerializer(canciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CancionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
