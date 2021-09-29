from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import reverse
from django.urls import reverse_lazy
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

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.empresa
        funcionario.save()
        return super(NovoFuncionario, self).form_valid(form)

    def get_success_url(self):
        return reverse('core:home')


class ListaFuncionarios(ListView):
    model = Funcionarios
    template_name = 'funcionarios/lista_funcionarios.html'


class DetalheFuncionario(DetailView):
    model = Funcionarios
    template_name = 'funcionarios/detalhe_funcionario.html'


class EditarFuncionario(UpdateView):
    form_class = FuncionarioChangeForm
    template_name = 'funcionarios/editar_funcionario.html'
    success_url = reverse_lazy('funcionarios:detalhe_funcionario')

    def get_object(self):
        return self.request.user
