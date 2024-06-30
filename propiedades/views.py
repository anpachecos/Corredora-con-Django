from django.shortcuts import render, redirect, get_object_or_404    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm, PropiedadForm
from .models import Propiedad, Comuna
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def ingresar(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'ingresar.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
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

def agendar_visita(request):
    return render(request, 'agendar_visita.html')

def property_grid(request):
    return render(request, 'property_grid.html')

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

@require_POST
def eliminar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, pk=propiedad_id)
    propiedad.delete()
    return redirect('listar_propiedad')
