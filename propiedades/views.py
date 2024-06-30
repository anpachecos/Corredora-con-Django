from django.shortcuts import render, redirect, get_object_or_404    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm
from .forms import PropiedadForm
from .models import Propiedad
from django.http import JsonResponse
from .models import Comuna

def ingresar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')

    return render(request, 'ingresar.html')

def registrarse(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
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

def listar_propiedad(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'listar_propiedad.html', {'propiedades': propiedades})

def agregar_propiedad(request, propiedad_id=None):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            propiedad = form.save()
            return redirect('agregar_propiedad') 
    else:
        form = PropiedadForm()

    return render(request, 'agregar_propiedad.html', {'form': form})

def comunas_por_region(request, region_id):
    comunas = Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse({'comunas': list(comunas)})