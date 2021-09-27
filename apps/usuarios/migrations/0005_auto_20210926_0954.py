# Generated by Django 3.2.7 on 2021-09-26 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
        ('usuarios', '0004_remove_usuarios_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='departamentos.departamentos'),
            preserve_default=False,
        ),
    ]
