from django.db import migrations


def cargar_canciones(apps, schema_editor):
    Cancion = apps.get_model('catalogo', 'Cancion')
    datos = [
        ('Bohemian Rhapsody', 'Queen', 1975, 'Rock'),
        ('Gracias a la vida', 'Violeta Parra', 1966, 'Folclor'),
        ('Billie Jean', 'Michael Jackson', 1982, 'Pop'),
    ]
    for titulo, artista, anio, genero in datos:
        Cancion.objects.using(schema_editor.connection.alias).get_or_create(
            titulo=titulo,
            artista=artista,
            defaults={'anio': anio, 'genero': genero},
        )


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_cancion'),
    ]

    operations = [
        migrations.RunPython(cargar_canciones, migrations.RunPython.noop),
    ]
