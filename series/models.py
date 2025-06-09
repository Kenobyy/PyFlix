from django.db import models

# Create your models here.


class Serie(models.Model):

    categorias_disponibles = [  # Establecemos una lista de categorías disponibles en la BBDD
        ('Acción', 'Acción'),
        ('Comedia', 'Comedia'),
        ('Drama', 'Drama'),
        ('Ciencia Ficción', 'Ciencia Ficción'),
        ('Fantasía', 'Fantasía'),
        ('Animación', 'Animación')
    ]

    titulo = models.CharField(max_length=40)              # Título de la serie
    argumento = models.CharField(max_length=800)          # Argumento de la serie
    creador = models.CharField(max_length=45, null=True)  # Creador de la serie
    duracion = models.IntegerField(null=True)             # Duración de cada capítulo
    num_capitulos = models.IntegerField(null=True)        # Número de capítulos totales de la serie
    num_temporadas = models.IntegerField(null=True)       # Númere de temporadas de la que consta la serie
    anio_estreno = models.IntegerField(null=True)         # Año de estreno de la serie
    categoria = models.CharField(max_length=20,           # Categoría de la serie
                                 choices=categorias_disponibles)
    favorito = models.BooleanField(default=False)         # Marca de favorito True / False
    vista = models.BooleanField(default=False)            # Marca de vista True / False
    imagen = models.ImageField(upload_to="series")        # Imagen de la serie
    enlace = models.CharField(max_length=200, null=True)  # Almacena el enlace HTTP a Youtube

    created = models.DateTimeField(auto_now_add=True)     # Agrega automáticamente la fecha de creación
    updated = models.DateTimeField(auto_now=True)         # Agrega automáticamete la fecha de edición

    class Meta:
        verbose_name = "serie"
        verbose_name_plural = "series"

    def __str__(self):
        return self.titulo
