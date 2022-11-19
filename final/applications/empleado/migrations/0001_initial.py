# Generated by Django 3.2 on 2022-11-19 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres del Empleado')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos del Empleado')),
                ('dni', models.CharField(max_length=50, verbose_name='DNI')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]