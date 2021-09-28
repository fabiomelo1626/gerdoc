from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


app_name = 'funcionarios'


urlpatterns = [
    path('novo-funcionario/', NovoFuncionario.as_view(), name='novo_funcionario'),
    path('lista-funcionarios/', ListaFuncionarios.as_view(), name='lista_funcionarios'),
]
