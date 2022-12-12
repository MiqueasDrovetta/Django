from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = (
            'apellidos',
            'nombres',
            'dni',
            'puesto',
        )
        widgets = {
            'puesto' : forms.Select(),
        }
        

