from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

app_name = 'empresas'


urlpatterns = [
    path('nova-empresa', login_required(NovaEmpresa.as_view()), name='nova_empresa'),
    path('lita-empresas', login_required(ListaEmpresas.as_view()), name='lista_empresas'),
]
