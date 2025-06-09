from django.shortcuts import render
from peliculas.models import Pelicula
from series.models import Serie
from django.shortcuts import redirect, get_object_or_404

# Create your views here.


def vistas(request):

    # Filtramos las películas y series donde el atributo 'vista' sea True
    lista_peliculas = Pelicula.objects.filter(vista=True)
    lista_series = Serie.objects.filter(vista=True)

    return render(request, "vistas/vistas.html", {"lista_peliculas": lista_peliculas,
                                                  "lista_series": lista_series})


def cambiar_pelicula_favorito(request, pelicula_id):

    # Obtenemos la película correspondiente según el ID
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)

    # Cambia el valor del campo "vista" de True a False o viceversa
    if request.method == "POST":
        pelicula.favorito = not pelicula.favorito
        pelicula.save()

    return redirect(f"/vistas/#favorito-btn-pelicula{pelicula.id}")


def cambiar_serie_favorito(request, serie_id):

    # Obtenemos la película correspondiente según el ID
    serie = get_object_or_404(Serie, pk=serie_id)

    # Cambia el valor del campo "vista" de True a False o viceversa
    if request.method == "POST":
        serie.favorito = not serie.favorito
        serie.save()

    return redirect(f"/vistas/#favorito-btn-serie{serie.id}")


def cambiar_pelicula_vista(request, pelicula_id):

    # Obtenemos la película correspondiente según el ID
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)

    # Cambia el valor del campo "vista" de True a False o viceversa
    if request.method == "POST":

        pelicula.vista = not pelicula.vista
        pelicula.save()

    return redirect(f"/vistas/#vista-btn-pelicula{pelicula.id}")


def cambiar_serie_vista(request, serie_id):

    # Obtenemos la serie correspondiente según el ID
    serie = get_object_or_404(Serie, pk=serie_id)

    # Cambia el valor del campo "vista" de True a False o viceversa
    if request.method == "POST":

        serie.vista = not serie.vista
        serie.save()

    return redirect(f"/vistas/#vista-btn-serie{serie.id}")