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
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filtrar las comunas si ya se ha seleccionado una región
        if self.instance.region:
            self.fields['comuna'].queryset = Comuna.objects.filter(region=self.instance.region).order_by('nombre')
        else:
            self.fields['comuna'].queryset = Comuna.objects.none()  # Mostrar ninguna comuna por defecto