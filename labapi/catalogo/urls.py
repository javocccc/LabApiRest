from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listar_libros),
    path('libros/crear/', views.crear_libro),
]