from django.forms import ModelForm, EmailInput

from personas.models import Persona

#EXTENDEMOS O MODIFICAMOS PARTE DE NUESTRA CLASE PARA QUE PUEDA SER POSIBLE
#ENTRAR A OTRO ENTORNO, ES DECIR, MODIFICAR A NUESTRO PLACER ESTE TIPO DE HTML

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'}),

        }

