from django import forms
from django.shortcuts import reverse
from .models import *
from .forms import *
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)


class NovoFuncionario(CreateView):
    form_class = FuncionarioCreateForm
    template_name = 'funcionarios/novo_funcionario.html'


    def get_success_url(self):
        return reverse('core:home')


class ListaFuncionarios(ListView):
    model = Funcionarios
    template_name = 'funcionarios/lista_funcionarios.html'
