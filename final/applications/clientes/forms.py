from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for ClienteForm."""

        model = Cliente
        fields = (
            'apellidos',
            'nombres',
            'dni',
            'direccion',
            'telefono',
            'fecha',
        )
