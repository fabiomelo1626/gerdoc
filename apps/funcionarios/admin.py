from django.contrib import admin
from apps.funcionarios.models import Funcionarios


@admin.register(Funcionarios)
class FuncionariosAdmin(admin.ModelAdmin):
    class Meta:
        model = Funcionarios
        fields = '__all__'
