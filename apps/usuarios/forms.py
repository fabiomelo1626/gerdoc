from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ('first_name', 'last_name', 'username',
                  'email', 'endereco', 'cpf', 'telefone', 'departamento',)


class UsuarioChangeForm(forms.UserChangeForm):
    class Meta:
        model = Usuarios
        fields = 'password',
