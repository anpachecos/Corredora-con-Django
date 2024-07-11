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



from django.shortcuts import render, get_object_or_404, redirect
from .models import Propiedad
from .forms import PropiedadForm



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
    if request.method == 'POST':
        propiedad_id = request.POST.get('propiedad_id')
        propiedad = Propiedad.objects.get(pk=propiedad_id)

        # Obtén la comuna del formulario (ejemplo)
        comuna_nombre = request.POST.get('comuna')
        
        # Verifica si ya existe una comuna con ese nombre
        comuna = get_object_or_404(Comuna, nombre=comuna_nombre)

        # Actualiza los campos según los datos del formulario
        propiedad.direccion_calle = request.POST.get('direccion', propiedad.direccion_calle)
        propiedad.comuna = comuna  # Asigna la comuna obtenida

        # Guarda la propiedad actualizada
        propiedad.save()
        return redirect('listar_propiedad')  # Redirige a la misma página después de guardar

    # Si no es POST, continuar con el procesamiento normal para mostrar la lista de propiedades
    propiedades = Propiedad.objects.all()
    return render(request, 'listar_propiedad.html', {'propiedades': propiedades})



def agregar_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            propiedad = form.save()
            mensaje = 'Propiedad agregada correctamente!'
            form = PropiedadForm()  # Limpiar el formulario para un nuevo ingreso
        else:
            mensaje = 'Ha ocurrido un error. Verifica los datos ingresados.'
    else:
        form = PropiedadForm()
        mensaje = None  # No mostrar ningún mensaje inicialmente
    
    context = {
        'form': form,
        'mensaje': mensaje,
    }
    return render(request, 'agregar_propiedad.html', context)

def get_comunas_por_region(request):
    region_id = request.GET.get('region')
    comunas = Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)


def comunas_por_region(request, region_id):
    comunas = Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse({'comunas': list(comunas)})

@require_POST
def eliminar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, pk=propiedad_id)
    propiedad.delete()
    return redirect('listar_propiedad')
