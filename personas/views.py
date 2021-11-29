from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona


def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    ##EN CASO DE QUE NO ENCUENTRE EL OBJETO O REGISTRO, MANDAR A LLAMAR LA ERROR 404
    #ESTA FUNCION RECIBE COMO PARAMETRO SU PK O SU ID, ES UTIL.
    #LA FUNCION REGRESA EL OBJETO COMPLETO, ES DECIR, SU NOMBRE, ID, ETC.
    persona = get_object_or_404(Persona, pk=id)
    #REGRESAMOS EL OBJETO DENTRO DE UN DICCIONARIO
    retorno = {'persona': persona}
    #PASAMOS COMO PARAMETRO EL DICCIONARIO CON EL OBJETO RECOGIDO, YA SEA 404 O NO
    return render(request, 'personas/detalle.html', retorno)

#PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona (request):
    #Tipo de request recibido POST o GET
    if request.method == 'POST':
        #Llenamos nuestro objeto Persona con el valor que recibimos de POST o GET
        formaPersona = PersonaForm(request.POST)
        #VALIDAMOS NUESTRO MODELO CREADO
        if formaPersona.is_valid():
            #SI FUE VALIDADO, LO GUARDAMOS Y REDIRIGIMOS A INDEX
            formaPersona.save()
            return redirect('index')
    #SI FUE GET, CREAMOS UNO VACIO PARA LLENAR
    else:
        #CREAMOS UN NUEVO MODELO VACIO, UNA PLANTILLA
        formaPersona = PersonaForm()
    #LLAMAMOS A RENDER, LA SOLICITUD, EL ARCHIVO A RENDERIZAR, EL OBJETO/VARIABLE A MANDAR
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editarPersona (request, id):
    # Recuperamos la informacion del objeto persona.
    persona = get_object_or_404(Persona, pk=id)
    # Tipo de request recibido POST o GET
    if request.method == 'POST':
        # Llenamos nuestro objeto Persona con el valor que recibimos de POST o GET, PERO LO CARGAMOS
        #CON LA INSTANCIA DE PERSONA, LA PRIMERA VARIABLE
        formaPersona = PersonaForm(request.POST, instance=persona)
        # VALIDAMOS NUESTRO MODELO CREADO
        if formaPersona.is_valid():
            # SI FUE VALIDADO, LO GUARDAMOS Y REDIRIGIMOS A INDEX
            formaPersona.save()
            return redirect('index')
    # SI FUE GET, CREAMOS UNO VACIO PARA LLENAR
    elif request.method == 'GET':
        #LLENAMOS EL TIPO DE INSTANCIA CON PERSONA, EL PREVIAMENTE CARGADO
        formaPersona = PersonaForm(instance=persona)
    # LLAMAMOS A RENDER, LA SOLICITUD, EL ARCHIVO A RENDERIZAR, EL OBJETO/VARIABLE A MANDAR
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

def eliminarPersona (request, id):
    # Recuperamos la informacion del objeto persona.
    persona = get_object_or_404(Persona, pk=id)
    #Si es valido
    if persona:
        #Solo lo borra
        persona.delete()
    #Volver a llamar a inicio/bienvenida
    return redirect('index')