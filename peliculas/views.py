from django.shortcuts import render
from peliculas.models import Pelicula
from django.shortcuts import redirect, get_object_or_404


# Create your views here.


def peliculas(request):

    lista_peliculas = Pelicula.objects.all()
    return render(request, "peliculas/peliculas.html", {"lista_peliculas": lista_peliculas})


def buscar_peliculas(request):
    query = request.GET.get('q')  # Obtiene el valor del parámetro 'q' del formulario
    categoria = request.GET.get('categoria')  # Obtiene el valor del parámetro 'categoria'

    if query:
        # Realiza la búsqueda de películas por nombre
        muestra_peliculas = Pelicula.objects.filter(titulo__icontains=query)
    else:
        # Si no se proporcionó un término de búsqueda, mostraremos todas las películas
        muestra_peliculas = Pelicula.objects.all()

    # Filtra las películas por categoría si se selecciona una categoría
    if categoria:
        muestra_peliculas = muestra_peliculas.filter(categoria=categoria)

    return render(request, 'peliculas/peliculas.html', {'lista_peliculas': muestra_peliculas})


def cambiar_vista(request, pelicula_id):

    # Obtenemos la película correspondiente según el ID
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)

    # Cambia el valor del campo "vista" de True a False o viceversa
    if request.method == "POST":

        pelicula.vista = not pelicula.vista
        pelicula.save()

    return redirect(f"/peliculas/#vista-btn-pelicula{pelicula.id -1}")


def cambiar_favorito(request, pelicula_id):

    # Obtenemos la película correspondiente según el ID
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)

    # Cambia el valor del campo "vista" de True a False o viceversa
    if request.method == "POST":
        pelicula.favorito = not pelicula.favorito
        pelicula.save()

    return redirect(f"/peliculas/#favorito-btn-pelicula{pelicula.id -1}")


def play_vista(request, pelicula_id):

    # Obtenemos la película correspondiente según el ID
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)

    # Cambia el valor del campo "vista" de True a False o viceversa
    if request.method == "POST":

        if not pelicula.vista:

            pelicula.vista = not pelicula.vista
            pelicula.save()

    # Redirige al usuario al enlace de la película
    return redirect(pelicula.enlace)






