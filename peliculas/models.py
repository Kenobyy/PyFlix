from django.db import models

# Create your models here.


class Pelicula(models.Model):

    categorias_disponibles = [          # Establecemos una lista de categorías disponibles en la BBDD
        ('Acción', 'Acción'),
        ('Comedia', 'Comedia'),
        ('Drama', 'Drama'),
        ('Ciencia Ficción', 'Ciencia Ficción'),
        ('Fantasía', 'Fantasía'),
    ]

    titulo = models.CharField(max_length=40)               # Título de la película
    argumento = models.CharField(max_length=800)           # Argumento de la película
    director = models.CharField(max_length=20)             # Director de la película
    duracion = models.IntegerField(null=True)              # Duración de la película en minutos ''
    anio_estreno = models.IntegerField(null=True)          # Año de estreno de la película
    categoria = models.CharField(max_length=20,            # Categoría de la película
                                 choices=categorias_disponibles)
    favorito = models.BooleanField(default=False)          # Marca de favorito True / False
    vista = models.BooleanField(default=False)             # Marca de vista True / False
    imagen = models.ImageField(upload_to="peliculas")      # Imagen de la película
    created = models.DateTimeField(auto_now_add=True)      # Agrega automáticamente la fecha de creación
    updated = models.DateTimeField(auto_now=True)          # Agrega automáticamete la fecha de edición
    enlace = models.CharField(max_length=200, null=True)   # Almacena el enlace HTTP a Youtube

    class Meta:

        verbose_name = "pelicula"
        verbose_name_plural = "peliculas"

    def __str__(self):

        return self.titulo
