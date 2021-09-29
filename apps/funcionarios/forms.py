from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from apps.funcionarios.models import Funcionarios


class FuncionarioCreateForm(UserCreationForm):
    class Meta:
        model = Funcionarios
        fields = (
            'first_name',
            'last_name',
            'cpf',
            'departamento',
            'logradouro',
            'numero',
            'bairro',
            'cep',
            'uf',
            'cidade',
            'email',
            'telefone',
            'username',
            'empresa',
        )


class FuncionarioChangeForm(UserChangeForm):
    class Meta:
        model = Funcionarios
        fields = (
            'first_name',
            'last_name',
            'cpf',
            'departamento',
            'logradouro',
            'numero',
            'bairro',
            'cep',
            'uf',
            'cidade',
            'email',
            'telefone',
        )
