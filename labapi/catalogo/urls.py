from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('libros', views.LibroViewSet, basename='libro')

urlpatterns = [
    path('canciones/', views.CancionList.as_view()),
    path('canciones/<int:pk>/', views.CancionDetail.as_view()),
    path('', include(router.urls)),
]
