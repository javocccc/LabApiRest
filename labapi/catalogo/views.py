from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"id": 2, "titulo": "La casa de los espíritus", "autor": "Isabel Allende", "anio": 1982},
    {"id": 3, "titulo": "Rayuela", "autor": "Julio Cortázar", "anio": 1963},
]