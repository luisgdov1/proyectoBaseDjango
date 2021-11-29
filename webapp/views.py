from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido (request):
    #ENTRAMOS A LOS METODOS DEL MODELO CREADO, Y QUE NO REGRESE SU INT DE CONTEO
    no_personas = Persona.objects.count()
    #MANDAMOS A TRAER A TODOS LOS OBJETOS QUE TENGAMOS DE PERSONAS
    personas = Persona.objects.all()
    #NUESTRO DICCIONARIO DE VARIABLES/PARAMETROS A MANDAR A HTML
    regreso =  {'no_personasss': no_personas, 'personas': personas}
    return render(request, 'Bienvenido.html', regreso)
