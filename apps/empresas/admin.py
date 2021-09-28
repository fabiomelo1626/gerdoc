from django.contrib import admin
from apps.empresas.models import Empresas


@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    class Meta:
        model = Empresas
        fields = '__all__'
