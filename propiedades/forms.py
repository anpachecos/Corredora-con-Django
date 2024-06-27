from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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