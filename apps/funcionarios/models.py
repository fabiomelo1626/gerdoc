from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.departamentos.models import Departamentos
from apps.empresas.models import Empresas


class Funcionarios(AbstractUser):
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    departamento = models.ForeignKey(Departamentos, on_delete=models.PROTECT, blank=True, null=True)
    logradouro = models.CharField('endereco', max_length=200, blank=True, null=True)
    numero = models.CharField('Numero', max_length=10, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9, blank=True, null=True)
    uf = models.CharField('UF', max_length=2)
    cidade = models.CharField('Cidade', max_length=100, blank=True, null=True)
    telefone = models.CharField('telefone', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
