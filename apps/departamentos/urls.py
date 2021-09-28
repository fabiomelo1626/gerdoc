from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


app_name = 'departamentos'


urlpatterns = [
    path('novo-departamento/', login_required(NovoDepartamento.as_view()), name='novo_departamento'),
    path('lista-departamentos/', login_required(ListaDepartamentos.as_view()), name='lista_departamentos'),
    path('detalhe-departamento/<int:pk>/', login_required(DetalheDepartamento.as_view()), name='detalhe_departamento'),
    path('editar-departamento/<int:pk>/', login_required(EditarDepartamento.as_view()), name='editar_departamento'),
    path('deletar-departamento/<int:pk>/', login_required(DeletarDepartamento.as_view()), name='deletar_departamento'),
]
