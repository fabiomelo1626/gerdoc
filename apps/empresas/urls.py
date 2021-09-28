from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

app_name = 'empresas'


urlpatterns = [
    path('nova-empresa/', login_required(NovaEmpresa.as_view()), name='nova_empresa'),
    path('lista-empresas/', login_required(ListaEmpresas.as_view()), name='lista_empresas'),
    path('detalhe-empresa/<int:pk>/', login_required(DetalheEmpresa.as_view()), name='detalhe_empresa'),
    path('editar-empresa/<int:pk>/', login_required(EditarEmpresa.as_view()), name='editar_empresa'),
    path('deletar-empresa/<int:pk>/', login_required(DeletarEmpresa.as_view()), name='deletar_empresa'),
]
