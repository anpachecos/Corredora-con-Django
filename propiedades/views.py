from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.db import IntegrityError


# Create your views here.
def home(request):
    return render(request, 'home.html')

def sobre_nosotros(request):
    return render(request, 'sobre-nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def ingresar(request):
    return render(request, 'ingresar.html')

def registrarse(request):

    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home') # redirect to task, con el return termina la función
            except IntegrityError:
                return render(request, 'registrarse.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'registrarse.html', {
                    'form': UserCreationForm,
                    "error": 'Las contraseñas no coinciden'
                })

def signout(request):
    logout(request)
    return redirect('home')
