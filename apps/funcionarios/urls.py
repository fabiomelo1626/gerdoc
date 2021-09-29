from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


app_name = 'funcionarios'


urlpatterns = [
    path('novo-funcionario/', NovoFuncionario.as_view(), name='novo_funcionario'),
    path('lista-funcionarios/', ListaFuncionarios.as_view(), name='lista_funcionarios'),
    path('detalhe-funcionario/<int:pk>/', DetalheFuncionario.as_view(), name='detalhe_funcionario'),
    path('editar-funcionario/', EditarFuncionario.as_view(), name='editar_funcionario'),
]
