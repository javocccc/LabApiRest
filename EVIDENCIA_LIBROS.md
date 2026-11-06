# Aporte de Libros para la evidencia del Laboratorio 7

Rama: `lab7-libros`, creada desde `main`.

El recurso Libro conserva los campos del Laboratorio 6: `titulo`, `autor` y `anio`. Las migraciones crean la tabla y cargan los tres libros de ejemplo. El modelo está registrado en el panel de administración. `LibroSerializer` es un `ModelSerializer` asociado a Libro.

## Comparación de código

Contando solo las líneas no vacías de las clases que implementan el CRUD en `catalogo/views.py`:

| Implementación | Líneas |
| --- | ---: |
| `LibroList` y `LibroDetail` con APIView, commit `439b1b3` | 24 |
| `LibroViewSet` con ModelViewSet, commit `0dac338` | 3 |

El ViewSet usa 21 líneas menos y mantiene las rutas `/api/libros/` y `/api/libros/<id>/`. Las rutas se conectan mediante `DefaultRouter`.

## Reflexión individual propuesta para revisar con tus palabras

Para este CRUD estándar prefiero `ModelViewSet`: permite listar, crear, consultar, actualizar y eliminar con una clase breve. Usaría `APIView` si cada operación necesitara reglas propias que no encajan bien en las acciones normales del ViewSet.

## Capturas que debes incorporar al Word grupal

1. `catalogo/models.py` mostrando `Libro`, `catalogo/serializers.py` mostrando `LibroSerializer` y `catalogo/admin.py` mostrando el registro.
2. `/api/libros/` con los tres libros de ejemplo y un POST que cree un cuarto libro.
3. `/api/libros/<id>/` mostrando GET, PUT y DELETE sobre ese cuarto libro.
4. El panel de administración con los libros cargados.

El CRUD se probó con `python manage.py test catalogo`: la misma prueba pasó con APIView y con ModelViewSet. Ejecuta `python manage.py migrate` en cada clon antes de iniciar el servidor.
