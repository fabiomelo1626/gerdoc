from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView
from .models import *


class NovaEmpresa(CreateView):
    model = Empresas
    fields = '__all__'
    template_name = 'empresas/nova_empresa.html'

    def get_success_url(self):
        return reverse('core:home')

class ListaEmpresas(ListView):
    model = Empresas
    template_name = 'empresas/lista_empresas.html'