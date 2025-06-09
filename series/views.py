from django.shortcuts import render
from series.models import Serie
from django.shortcuts import redirect, get_object_or_404


# Create your views here.


def series(request):

    lista_series = Serie.objects.all()
    return render(request, "series/series.html", {"lista_series": lista_series})


def buscar_series(request):

    query = request.GET.get('q')                   # Obtiene el valor del parámetro 'q' del formulario
    categoria = request.GET.get('categoria')       # Obtiene el valor del parámetro 'categoria'

    if query:
        # Realiza la búsqueda de películas por nombre
        muestra_series = Serie.objects.filter(titulo__icontains=query)
    else:
        # Si no se proporciona un término de búsqueda, mostraremos todas las series
        muestra_series = Serie.objects.all()

    # Filtra las series por categoría si se selecciona una categoría
    if categoria:
        muestra_series = muestra_series.filter(categoria=categoria)

    return render(request, 'series/series.html', {'lista_series': muestra_series})


def cambiar_vista_serie(request, serie_id):

    # Obtenemos la película correspondiente según el ID
    serie = get_object_or_404(Serie, pk=serie_id)

    # Cambia el valor del campo "vista" de True a False o viceversa
    if request.method == "POST":

        serie.vista = not serie.vista
        serie.save()

    return redirect(f"/series/#vista-btn-serie{serie.id -1}")


def cambiar_favorito_serie(request, serie_id):

    # Obtenemos la película correspondiente según el ID
    serie = get_object_or_404(Serie, pk=serie_id)

    # Cambia el valor del campo "vista" de True a False o viceversa
    if request.method == "POST":
        serie.favorito = not serie.favorito
        serie.save()
        print("Guardado", serie.favorito)

    return redirect(f"/series/#favorito-btn-serie{serie.id -1}")
