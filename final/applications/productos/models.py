from django.db import models

# Create your models here.
class Unidad(models.Model):
    """Model definition for Unidad."""

    # TODO: Define fields here
    unidad = models.CharField("Unidad del Producto", max_length=50)
    desunidad = models.CharField("Descripcion de la unidad", max_length=50)

    class Meta:
        """Meta definition for Unidad."""

        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        """Unicode representation of Unidad."""
        return self.unidad

class Marca(models.Model):
    """Model definition for Marca."""

    # TODO: Define fields here
    marca = models.CharField("Marca del Producto", max_length=50)

    class Meta:
        """Meta definition for Marca."""

        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        """Unicode representation of Marca."""
        return self.marca

class Categoria(models.Model):
    """Model definition for Categoria."""

    # TODO: Define fields here
    categoria = models.CharField("Categoria del Producto", max_length=50)
    descategoria = models.CharField("Descripcion de la categoria", max_length=50)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.categoria
        
class Producto(models.Model):
    """Model definition for Producto."""

    # TODO: Define fields here
    codigo = models.CharField("Codigo del Producto", max_length=50)
    nombre = models.CharField("Nombre del Producto", max_length=50)
    descripcion = models.CharField("Descripcion del Producto", max_length=50)
    unidad = models.ManyToManyField(Unidad)
    marca = models.ManyToManyField(Marca)
    categoria = models.ManyToManyField(Categoria)
    precioVenta = models.FloatField("Precio Venta del producto", max_length=10)
    precioCompra = models.FloatField("Precio Compra del producto", max_length=10)
    stock = models.IntegerField("Stock del producto")
    

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Producto."""
        return f'{self.codigo}, {self.nombre[0:9]}, Precio:{self.precioVenta}'






