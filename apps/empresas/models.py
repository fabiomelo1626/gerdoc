from django.db import models


class Empresas(models.Model):
    razao_social = models.CharField('Razao Social', max_length=100, unique=True)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18, unique=True)
    logradouro = models.CharField('Endereco', max_length=200)
    numero = models.CharField('Numero', max_length=10, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True, null=True)
    uf = models.CharField('UF', max_length=2)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=15)

    def __str__(self):
        return self.razao_social
