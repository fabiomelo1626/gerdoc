from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .models import *


class NovoDepartamento(CreateView):
    model = Departamentos
    template_name = 'departamentos/novo_departamento.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('core:home')
