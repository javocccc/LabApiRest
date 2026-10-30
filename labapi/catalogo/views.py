from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"id": 2, "titulo": "La casa de los espíritus", "autor": "Isabel Allende", "anio": 1982},
    {"id": 3, "titulo": "Rayuela", "autor": "Julio Cortázar", "anio": 1963},
]

@api_view(['GET'])
def listar_libros(request):
    return Response(libros)

@api_view(['POST'])
def crear_libro(request):
    nuevo_id = max([l["id"] for l in libros], default=0) + 1
    nuevo = {
        "id": nuevo_id,
        "titulo": request.data.get("titulo"),
        "autor": request.data.get("autor"),
        "anio": request.data.get("anio"),
    }
    libros.append(nuevo)
    return Response(nuevo, status=status.HTTP_201_CREATED)