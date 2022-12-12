from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Productoform."""

        model = Producto
        fields = (
            'codigo',
            'nombre',
            'descripcion',
            'unidad',
            'marca',
            'categoria',
            'precioVenta',
            'precioCompra',
            'stock',
            
        )
        widgets = {
            'unidad' : forms.Select(),
            'marca' : forms.Select(),
            'categoria' : forms.Select(),
        }
        

