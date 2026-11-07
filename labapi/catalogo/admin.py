from django.contrib import admin

from .models import Cancion, Libro

admin.site.register(Libro)
admin.site.register(Cancion)
