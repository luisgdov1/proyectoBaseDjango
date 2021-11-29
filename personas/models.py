from django.db import models

# Create your models here.

#ESTO ES COMO CREAR NUESTRO PROPIA SECUENCIA DE SQL, NUESTRA PLANTILLA DE DATOS

#CADA CLASE ES UNA NUEVA TABLA DE SQL, EN SINTESIS.
class Domicilio(models.Model):
    #REVISAMOS LA DOCUMENTACION EN CASO DE OTRO TIPO, EJEMPLO PARA BYTES O ALGO ASI.
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    #AQUI ES COMO MODIFICAR EL STR() BASICO, SOLO QUE CON FORMATO
    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #IMPORTANTE, PARA LAS CLAVES FORANEAS O UNIR VARIAS TABLAS, SE UTILIZA ESTOS PARAMETROS
    #BASICOS, ON DELETE [COMMO VA A SER BORRADO, SI EN CASCADA O NO], #SI ES VALIDO UN VALOR NULO
    #
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return  f'Persona id: {self.id}: {self.nombre}, {self.apellido}, {self.email} '
