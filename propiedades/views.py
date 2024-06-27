from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm



def ingresar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Cambia 'home' por la URL a la que deseas redirigir tras el inicio de sesión
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')

    return render(request, 'ingresar.html')

def registrarse(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Cambia 'home' por la URL a la que deseas redirigir tras el registro
    else:
        form = UserRegistrationForm()

    return render(request, 'registrarse.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def sobre_nosotros(request):
    return render(request, 'sobre-nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def signout(request):
    logout(request)
    return redirect('home')

