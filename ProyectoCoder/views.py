from django.http import HttpResponse
from django.template import Template, Context
from setuptools import *

def saludo(request):
    return HttpResponse("Hola, mundo. Esta es mi primera página web.")

def probando_templates(request, name):
    mi_html = open("""C:/Users/ANDREABRITO/Desktop/Python_Projects/ProyectoCoder/templates/template1.html""")
    platilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({"name": name}) # Contexto vacío, el contexto es un diccionario, sirve para pasar variables a la plantilla
    
    documento = platilla.render(mi_contexto)

    return HttpResponse(documento)