from django.db import models
from apps.empresas.models import Empresas


class Departamentos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

