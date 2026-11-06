from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.LibroList.as_view()),
    path('canciones/', views.listar_canciones),
    path('canciones/crear/', views.crear_cancion),
]
