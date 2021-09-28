from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
)


class NovaEmpresa(CreateView):
    form_class = EmpresasForm
    template_name = 'empresas/nova_empresa.html'

    def get_success_url(self):
        return reverse('empresas:lista_empresas')


class ListaEmpresas(ListView):
    model = Empresas
    template_name = 'empresas/lista_empresas.html'


class DetalheEmpresa(DetailView):
    model = Empresas
    template_name = 'empresas/detalhe_empresa.html'


class DeletarEmpresa(DeleteView):
    model = Empresas
    template_name = 'empresas/confirme_delete_empresa.html'
    success_url = reverse_lazy('empresas:lista_empresas')
