import os

from peliculas.models import Pelicula
from series.models import Serie
from django.db.models import Sum, ExpressionWrapper, IntegerField, F
from django.db import models
from django.shortcuts import render
from django.conf import settings
import plotly.graph_objs as go
from plotly.offline import plot


# Create your views here.


def estadisticas(request):

    return render(request, "estadisticas/estadisticas.html")


def generar_grafica_pelis_y_series_vistas(request):

    # Consulta para obtener el número total de películas vistas
    num_peliculas_vistas = Pelicula.objects.filter(vista=True).count()

    # Consulta para obtener el número total de series vistas
    num_series_vistas = Serie.objects.filter(vista=True).count()

    # Crear un gráfico de barras simple con Plotly
    categorias = ["Películas", "Series"]
    valores = [num_peliculas_vistas, num_series_vistas]

    # Personaliza el aspecto del gráfico de barras
    data = [
        go.Bar(
            x=categorias,
            y=valores,
            marker=dict(
                color=['#8F5FBB', '#675FBB'],
                line=dict(
                    color='#130C1E',  # Color de los bordes de las barras
                    width=3  # Ancho de los bordes de las barras
                )
            ),
            textfont=dict(
                family='Arial',  # Fuente del texto
                size=16,  # Tamaño del texto
                color='white'  # Color del texto
            )
        )
    ]
    layout = go.Layout(
        xaxis=dict(title='Categorías', tickfont=dict(size=16)),
        yaxis=dict(title='Número Total', tickfont=dict(size=16)),
        title='NÚMERO TOTAL PELICULAS Y SERIES VISTAS',
        width=700,  # Ancho personalizado
        height=500,  # Alto personalizado
        margin=dict(l=50, r=50, b=50, t=50),
        paper_bgcolor='#160F31', font={'color': 'white'},
        plot_bgcolor='#1E1638',
    )
    fig = go.Figure(data=data, layout=layout)

    # Obtener el gráfico como un HTML y establecerlo en el contexto
    graph = plot(fig, output_type='div')

    # Establecemo la variable en True si la gráfica se ha generado con éxito
    grafica_generada_2 = True

    return render(request, 'estadisticas/estadisticas.html',
                  {'grafica_vistas_html': graph,
                   'grafica_generada_2': grafica_generada_2})


def generar_grafica_duracion(request):

    # Consulta para obtener la suma de la duración de las películas vistas
    duracion_total_peliculas_vistas = Pelicula.objects.filter(vista=True).aggregate(total_duracion=Sum('duracion'))

    # Consulta para obtener la suma de la duración total multiplicada por el número de
    # capítulos en todas las series vistas
    duracion_total_series_vistas = Serie.objects.filter(vista=True).annotate(
        duracion_total=ExpressionWrapper(
            F('duracion') * F('num_capitulos'),
            output_field=IntegerField()
        )
    ).aggregate(total_duracion=Sum('duracion_total'))

    # Datos de las dos categorias del grafico de barras
    categorias = ["Películas", "Series"]

    # Convertir la duración de minutos a horas
    duracion_peliculas_horas = (duracion_total_peliculas_vistas['total_duracion'] or 0) / 60.0
    duracion_series_horas = (duracion_total_series_vistas['total_duracion'] or 0) / 60.0

    valores = [duracion_peliculas_horas, duracion_series_horas]

    # Creamos un gráfico de barras con Plotly
    data = [go.Bar(x=categorias, y=valores, marker=dict(color=['#8F5FBB', '#675FBB'], line=dict(
                    color='#130C1E',  # Color de los bordes de las barras
                    width=3)))]  # Ancho de los bordes de las barras)]
    layout = go.Layout(
        xaxis=dict(title='Categorías', tickfont=dict(size=16)),
        yaxis=dict(title='Duración Total (Horas)', tickfont=dict(size=16)),
        title='TIEMPO EMPLEADO EN VER PELICULAS Y SERIES (Horas)',
        width=700,  # Ancho personalizado
        height=500,  # Alto personalizado,
        margin=dict(l=50, r=50, b=50, t=50, autoexpand=True),
        paper_bgcolor='#160F31', font={'color': 'white'},
        plot_bgcolor='#1E1638',
    )
    fig = go.Figure(data=data, layout=layout)

    # Obtener el gráfico como un HTML y establecerlo en el contexto
    graph = plot(fig, output_type='div')

    # Establece esto en True si la gráfica se ha generado con éxito
    grafica_generada = True

    return render(request, 'estadisticas/estadisticas.html', {'imagen_grafica': graph,
                                                              'grafica_generada': grafica_generada})


def generar_grafica_categoria(request):

    # Consulta para obtener el recuento de películas de cada categoría que se han visto.
    peliculas_vistas_por_categoria = Pelicula.objects.filter(vista=True).values('categoria').annotate(
        total=models.Count('categoria'))

    # Consulta para obtener el recuento de series de cada categoría que se han visto.
    series_vistas_por_categoria = Serie.objects.filter(vista=True).values('categoria').annotate(
        total=models.Count('categoria'))

    # Creamos una listas de categorías y recuentos para las películas.
    categorias_peliculas = [item['categoria'] for item in peliculas_vistas_por_categoria]
    recuento_peliculas = [item['total'] for item in peliculas_vistas_por_categoria]

    # Creamos una listas de categorías y recuentos para las series.
    categorias_series = [item['categoria'] for item in series_vistas_por_categoria]
    recuento_series = [item['total'] for item in series_vistas_por_categoria]

    # Crear un gráfico de tarta para películas.
    grafica_peliculas = go.Figure(data=[go.Pie(labels=categorias_peliculas, values=recuento_peliculas,
                                               textinfo='percent+label',
                                               textfont=dict(size=14),
                                               pull=[0.1, 0.1, 0.1, 0.1])])
    grafica_peliculas.update_layout(title='% PELICULAS VISTAS EN CADA CATEGORÍA', width=500, height=500,
                                    paper_bgcolor='#160F31', font={'color': 'white'})

    # Crear un gráfico de tarta para series.
    grafica_series = go.Figure(data=[go.Pie(labels=categorias_series, values=recuento_series,
                                            textinfo='percent+label',
                                            textfont=dict(size=14),
                                            pull=[0.1, 0.1, 0.1, 0.1])])
    grafica_series.update_layout(title='% SERIES VISTAS EN CADA CATEGORÍA', width=500, height=500,
                                 paper_bgcolor='#160F31', font={'color': 'white'})

    # Convertir los gráficos a HTML
    grafica_peliculas_html = plot(grafica_peliculas, output_type='div')
    grafica_series_html = plot(grafica_series, output_type='div')

    # Establecer esto en True si la gráfica se ha generado con éxito
    grafica_generada_3 = True

    return render(request, 'estadisticas/estadisticas.html', {
        'categoria_pelis': grafica_peliculas_html,
        'categoria_series': grafica_series_html,
        'grafica_generada_3': grafica_generada_3
    })
