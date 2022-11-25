# Generated by Django 3.2 on 2022-11-25 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria del Producto')),
                ('descategoria', models.CharField(max_length=50, verbose_name='Descripcion de la categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca del Producto')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=50, verbose_name='Unidad del Producto')),
                ('desunidad', models.CharField(max_length=50, verbose_name='Descripcion de la unidad')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='Codigo del Producto')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Producto')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion del Producto')),
                ('precioVenta', models.FloatField(max_length=10, verbose_name='Precio Venta del producto')),
                ('precioCompra', models.FloatField(max_length=10, verbose_name='Precio Compra del producto')),
                ('stock', models.IntegerField(verbose_name='Stock del producto')),
                ('categoria', models.ManyToManyField(to='productos.Categoria')),
                ('marca', models.ManyToManyField(to='productos.Marca')),
                ('unidad', models.ManyToManyField(to='productos.Unidad')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]