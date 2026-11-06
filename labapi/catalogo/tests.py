from rest_framework import status
from rest_framework.test import APITestCase

from .models import Libro


class LibroAPITests(APITestCase):
    def test_crud_completo(self):
        ruta = '/api/libros/'
        datos = {'titulo': 'El túnel', 'autor': 'Ernesto Sábato', 'anio': 1948}

        listado = self.client.get(ruta)
        self.assertEqual(listado.status_code, status.HTTP_200_OK)
        self.assertEqual(len(listado.data), 3)

        creado = self.client.post(ruta, datos, format='json')
        self.assertEqual(creado.status_code, status.HTTP_201_CREATED)
        pk = creado.data['id']
        detalle = f'{ruta}{pk}/'
        self.assertEqual(self.client.get(detalle).data['titulo'], 'El túnel')

        actualizado = self.client.put(
            detalle, {**datos, 'anio': 1949}, format='json'
        )
        self.assertEqual(actualizado.status_code, status.HTTP_200_OK)
        self.assertEqual(Libro.objects.get(pk=pk).anio, 1949)

        eliminado = self.client.delete(detalle)
        self.assertEqual(eliminado.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Libro.objects.filter(pk=pk).exists())

# Create your tests here.
