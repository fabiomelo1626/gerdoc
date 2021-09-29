from django import forms
from apps.empresas.models import Empresas


class EmpresasForm(forms.ModelForm):
    razao_social = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
            }
        )
    )

    nome_fantasia = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
            }
        )
    )

    cnpj = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
            }
        )
    )

    endereco = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
            }
        )
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
            }
        )
    )

    class Meta:
        model = Empresas
        fields = (
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'endereco',
            'email',
            'telefone',
        )
