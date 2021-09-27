from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


app_name = 'departamentos'


urlpatterns = [
    path('novo-departamento', login_required(NovoDepartamento.as_view()), name='novo_departamento')
]
