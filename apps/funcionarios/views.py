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

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.empresa
        funcionario.save()
        return super(NovoFuncionario, self).form_valid(form)

    def get_success_url(self):
        return reverse('core:home')


class ListaFuncionarios(ListView):
    model = Funcionarios
    template_name = 'funcionarios/lista_funcionarios.html'
