from django.urls import path
from .views import VRegistro, cerrar_sesion, logear


urlpatterns = [

    # Mostramos la clase VRegistro como una vista
    path("", VRegistro.as_view(), name="Autenticacion"),
    path("cerrar_sesion", cerrar_sesion, name="cerrar_sesion"),
    path("logear", logear, name="logear"),

]
