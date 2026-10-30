from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listar_libros),
    path('libros/crear/', views.crear_libro),
]

from django.urls import path
from . import views

urlpatterns = [
    path('canciones/', views.listar_canciones),
    path('canciones/crear/', views.crear_cancion),
]