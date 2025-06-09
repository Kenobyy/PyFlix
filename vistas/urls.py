from django.urls import path
from . import views

app_name = 'vistas'

urlpatterns = [

    path("", views.vistas, name="Vistas"),
    path("cambiar_pelicula_favorito/<int:pelicula_id>/", views.cambiar_pelicula_favorito,
         name="cambiar_pelicula_favorito"),
    path("cambiar_serie_favorito/<int:serie_id>/", views.cambiar_serie_favorito,
         name="cambiar_serie_favorito"),
    path("cambiar_pelicula_vista/<int:pelicula_id>/", views.cambiar_pelicula_vista,
         name="cambiar_pelicula_vista"),
    path("cambiar_serie_vista/<int:serie_id>/", views.cambiar_serie_vista,
         name="cambiar_serie_vista"),

]



