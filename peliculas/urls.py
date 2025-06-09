from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", views.peliculas, name="Peliculas"),
    path("cambiar_vista/<int:pelicula_id>/", views.cambiar_vista, name = "cambiar_vista"),
    path("cambiar_favorito/<int:pelicula_id>/", views.cambiar_favorito, name = "cambiar_favorito"),
    path('buscar_peliculas/', views.buscar_peliculas, name='buscar_peliculas'),
    path("play_vista/<int:pelicula_id>/", views.play_vista, name="play_vista"),

]
