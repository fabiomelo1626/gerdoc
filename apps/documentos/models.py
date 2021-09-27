from django.db import models
from apps.departamentos.models import Departamentos
from apps.usuarios.models import Usuarios


class Requerimentos(models.Model):
    de = models.CharField('De', max_length=100)
    para = models.CharField('Para', max_length=100)
    assunto = models.CharField('Assunto', max_length=100)
    conteudo = models.TextField('Conteudo', max_length=100)

    def __str__(self):
        return self.assunto
