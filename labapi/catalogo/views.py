from rest_framework import viewsets

from .models import Cancion, Libro
from .serializers import CancionSerializer, LibroSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('id')
    serializer_class = LibroSerializer


class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all().order_by('id')
    serializer_class = CancionSerializer
