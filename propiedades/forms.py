from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Propiedad, Region, Comuna

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        help_text='Tu contraseña debe tener más de 8 caractéres'
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput,
        help_text='Ingresa la misma contraseña.'
    )

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        labels = {
            'username': 'Username',
        }
        
class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'  # Puedes cambiar '__all__' por una lista de campos específicos si lo prefieres