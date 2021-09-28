from django.contrib import admin
from apps.departamentos.models import Departamentos


@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
    class Meta:
        model = Departamentos
        fields = '__all__'
