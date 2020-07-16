from django.http import HttpResponse
import datetime
from django.template import Template,Context

class persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo(request):
    p1=persona("kevin","xcar")
    #temas_curso=["Django","Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    #doc_externo=open("C:/Users/Prueba/Desktop/Poyecto restaurante2/Proyecto1/Proyecto1/Plantillas/primera_plantilla.html")
    #planti=Template(doc_externo.read())
    #doc_externo.close()
    #cx=Context({"Temas":temas_curso,"nombre_persona":p1.nombre})
    #documento=planti.render(cx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Gracias por todo") 