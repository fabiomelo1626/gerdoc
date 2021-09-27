from django.contrib import admin
from .models import *


@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
    class Meta:
        model = Departamentos
        fields = '__all__'
