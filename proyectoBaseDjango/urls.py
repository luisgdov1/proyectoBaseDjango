"""proyectoBaseDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#Aplicaciones las mandamos a importar donde se encuentra, las APP se interconectan,
#si queremos
from webapp.views import bienvenido
from personas.views import detallePersona, nuevaPersona, editarPersona, eliminarPersona

urlpatterns = [
    #URL, les podemos pasar un parametro o indicar un nombre para mas facilidad
    path('admin/', admin.site.urls),
    #ejemplo de url con NOMBRE
    path('', bienvenido, name='index'),
    #EJEMPLO DE URL PASANDO UN PARAMETRO.
    path('detalle_persona/<int:id>', detallePersona),
    path('nueva_persona', nuevaPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona)
]
