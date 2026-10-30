from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

canciones = [
    {"id": 1, "titulo": "Bohemian Rhapsody", "artista": "Queen", "anio": 1975, "genero": "Rock"},
    {"id": 2, "titulo": "Gracias a la vida", "artista": "Violeta Parra", "anio": 1966, "genero": "Folclor"},
    {"id": 3, "titulo": "Billie Jean", "artista": "Michael Jackson", "anio": 1982, "genero": "Pop"},
]