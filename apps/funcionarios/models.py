from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.departamentos.models import Departamentos
from apps.empresas.models import Empresas


class Funcionarios(AbstractUser):
    departamento = models.ForeignKey(Departamentos, on_delete=models.PROTECT, null=True, blank=True)
    endereco = models.CharField('endereco', max_length=200, blank=True, null=True)
    telefone = models.CharField('telefone', max_length=15, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)

    def __str__(self):
        return self.username
