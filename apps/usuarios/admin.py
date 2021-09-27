from django.contrib import admin
from .models import *


@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    class Meta:
        model = Usuarios
        fields = '__all__'
