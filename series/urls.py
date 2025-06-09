from django.urls import path
from . import views

urlpatterns = [

    path('', views.series, name="Series"),
    path("cambiar_vista_serie/<int:serie_id>/", views.cambiar_vista_serie, name="cambiar_vista_serie"),
    path("cambiar_favorito_serie/<int:serie_id>/", views.cambiar_favorito_serie, name="cambiar_favorito_serie"),
    path('buscar_series/', views.buscar_series, name='buscar_series'),

]
