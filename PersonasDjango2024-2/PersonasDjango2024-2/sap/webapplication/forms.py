# Importo el módulo de formularios de Django para crear formularios basados en modelos.
from django import forms

# Importo el modelo Persona desde el archivo models.py de la aplicación personas.
from personas.models import Persona

# Heredo de forms.ModelForm para utilizar las funcionalidades del formulario basado en un modelo.
class PesonaForm(forms.ModelForm):

    # Clase interna que proporciona metainformación sobre el formulario.
    class Meta:
        # Especifico el modelo que se utilizará para generar el formulario.
        # En este caso, el modelo Persona.
        model=Persona
        # Lista de campos del modelo Persona que se incluirán en el formulario.
        fields=['nombre','apellido','email']


