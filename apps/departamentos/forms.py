from django import forms
from apps.departamentos.models import Departamentos


class DepartamentosForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
            }
        )
    )

    widget = {
        'empresa': forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
    }

    class Meta:
        model = Departamentos
        fields = (
            'nome',
            'empresa',
        )
