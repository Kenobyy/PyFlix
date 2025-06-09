from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


# Creamos una clase para crear el GET y el POST, VistaRegistro
class VRegistro(View):

    # Esta función se va a encargar de mostrarnos el formulario de registro de usuarios
    def get(self, request):

        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    # Esta función va a gestionar el envío de la información del usuario a través de formulario
    def post(self, request):

        form = UserCreationForm(request.POST)

        if form.is_valid():

            # En esta variable almacenamos la información del usuario, siempre que el formulario no de error
            usuario = form.save()

            login(request, usuario)

            return redirect("Inicio")

        else:

            # En caso de que el formulario no sea válido, mostramos un mensaje de error
            for mensage in form.error_messages:

                messages.error(request, form.error_messages[mensage])

            return render(request, "registro/registro.html", {"form": form})


# Función para cerrar sesion
def cerrar_sesion(request):

    logout(request)

    return redirect("Inicio")


def logear(request):

    # Comprobamos si se ha pulsado el boton LOGEAR
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        # Comprobamos que la información se ha introducido correctamente
        if form.is_valid():

            nombre_usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = clave)

            # Comprobamos que el usuario es correcto
            if usuario is not None:

                login(request, usuario)
                return redirect("Inicio")

            else:
                messages.error(request, "Usuario no válido")

        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos")

    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})

