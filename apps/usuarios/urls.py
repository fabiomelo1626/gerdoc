from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


app_name = 'usuarios'


urlpatterns = [
    path('novo-usuario', NovoUsuario.as_view(), name='novo_usuario'),
]
