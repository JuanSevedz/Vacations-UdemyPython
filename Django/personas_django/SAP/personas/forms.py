from django.forms import ModelForm, EmailInput

from personas.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        """
        Meta -> Se usa para validar el formato del correo que se ingrese cuando se crea un nuevo usuario
        """
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }