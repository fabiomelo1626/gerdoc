from django import forms
from django.views.generic import CreateView
from django.shortcuts import reverse
from .forms import *
from .models import *


class NovoUsuario(CreateView):
    form_class = UsuarioCreateForm
    template_name = 'usuarios/novo_usuario.html'


    def get_success_url(self):
        return reverse('core:home')
