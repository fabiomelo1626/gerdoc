from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from apps.funcionarios.models import Funcionarios


class FuncionarioCreateForm(UserCreationForm):
    class Meta:
        model = Funcionarios
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'logradouro',
            'numero',
            'bairro',
            'cep',
            'cidade',
            'uf',
            'cpf',
            'telefone',
            'empresa',
        )


class FuncionarioChangeForm(forms.UserChangeForm):
    class Meta:
        model = Funcionarios
        fields = 'password',
