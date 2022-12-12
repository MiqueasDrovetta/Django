from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    """Form definition for Proveedor."""

    class Meta:
        """Meta definition for Proveedorform."""

        model = Proveedor
        fields = (
            'nombres',
            'representante',
            'cuit',
            'direccion',
            'telefono',
            'email',
            'fecha',
        )
        

