from django import forms
from .models import *


class DocumentosForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = '__all__'
