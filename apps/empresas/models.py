from django.db import models


class Empresas(models.Model):
    razao_social = models.CharField('Razao Social', max_length=100, unique=True)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=15, unique=True)
    endereco = models.CharField('Endereco', max_length=200)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=14)

    def __str__(self):
        return self.razao_social
