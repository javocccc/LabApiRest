from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    anio = models.IntegerField()

    def __str__(self):
        return self.titulo


class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    anio = models.IntegerField()
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
