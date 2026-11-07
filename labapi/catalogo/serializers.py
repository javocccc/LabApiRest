from rest_framework import serializers

from .models import Cancion, Libro


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'anio']
        read_only_fields = ['id']


class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = ['id', 'titulo', 'artista', 'anio', 'genero']
        read_only_fields = ['id']
