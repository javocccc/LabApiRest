from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Libro
from .serializers import LibroSerializer


class LibroList(APIView):
    def get(self, request):
        libros = Libro.objects.all().order_by('id')
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


canciones = [
    {"id": 1, "titulo": "Bohemian Rhapsody", "artista": "Queen", "anio": 1975, "genero": "Rock"},
    {"id": 2, "titulo": "Gracias a la vida", "artista": "Violeta Parra", "anio": 1966, "genero": "Folclor"},
    {"id": 3, "titulo": "Billie Jean", "artista": "Michael Jackson", "anio": 1982, "genero": "Pop"},
]

@api_view(['GET'])
def listar_canciones(request):
    return Response(canciones)

@api_view(['POST'])
def crear_cancion(request):
    nuevo_id = max([c["id"] for c in canciones], default=0) + 1
    nueva = {
        "id": nuevo_id,
        "titulo": request.data.get("titulo"),
        "artista": request.data.get("artista"),
        "anio": request.data.get("anio"),
        "genero": request.data.get("genero"),
    }
    canciones.append(nueva)
    return Response(nueva, status=status.HTTP_201_CREATED)
