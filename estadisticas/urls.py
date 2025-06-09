from django.urls import path
from . import views
from .views import generar_grafica_duracion, generar_grafica_pelis_y_series_vistas, generar_grafica_categoria

urlpatterns = [

    path("", views.estadisticas, name="Estadisticas"),
    path('generar_grafica_duracion/', generar_grafica_duracion, name='generar_grafica'),
    path('generar_grafica_pelis_y_series_vistas/', generar_grafica_pelis_y_series_vistas,
         name='generar_grafica_pelis_y_series_vistas'),
    path('generar_grafica_categoria/', generar_grafica_categoria,
         name='generar_grafica_categoria'),
]
