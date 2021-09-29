from django.shortcuts import render, reverse
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


class NovoDepartamento(CreateView):
    form_class = DepartamentosForm
    template_name = 'departamentos/novo_departamento.html'

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.empresa
        departamento.save()
        return super(NovoDepartamento, self).form_valid(form)

    def get_success_url(self):
        return reverse('departamentos:lista_departamentos')


class ListaDepartamentos(ListView):
    model = Departamentos
    template_name = 'departamentos/lista_departamentos.html'


class DetalheDepartamento(DetailView):
    model = Departamentos
    template_name = 'departamentos/detalhe_departamento.html'


class EditarDepartamento(UpdateView):
    model = Departamentos
    template_name = 'departamentos/editar_departamento.html'
    fields = (
        'nome',
        'empresa',
    )


class DeletarDepartamento(DeleteView):
    model = Departamentos
    template_name = 'departamentos/confirme_delete_departamento.html'
    success_url = reverse_lazy('departamentos:lista_departamentos')
