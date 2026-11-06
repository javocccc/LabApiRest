from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('libros', views.LibroViewSet, basename='libro')

urlpatterns = [
    path('canciones/', views.listar_canciones),
    path('canciones/crear/', views.crear_cancion),
    path('', include(router.urls)),
]
