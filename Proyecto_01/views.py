import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def paginaSaluda(request): #Primera vista

    nombre = 'David'
    apellido = 'Star'
    edad = '43'
    fecha = datetime.datetime.now()
    lista_cursos = []

    #doc_externo = open('D:/hp/django-pildoras/Proyecto_01/Proyecto_01/plantillas/miPlantilla.html')
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #mi_plantilla = loader.get_template('miPlantilla.html')

    #ctx = Context({'nombre_usuario': nombre,'apellido_usuario': apellido,'edad_usuario': edad,'fecha': fecha,'cursos': lista_cursos})

    ctx = {
        'nombre_usuario': nombre,
        'apellido_usuario': apellido,
        'edad_usuario': edad,
        'fecha': fecha,
        'cursos': lista_cursos
    }

    #documento = mi_plantilla.render(ctx)

    return render(request, 'miPlantilla.html', ctx)

def zapatos(request):
    fecha = datetime.datetime.now()

    return render(request, 'ApartadoZapatos.html', {'fecha': fecha})

def camisas(request):
    fecha = datetime.datetime.now()

    return render(request, 'ApartadoCamisas.html', {'fecha': fecha})

def paginaDespide(request): #segunda vista
    return HttpResponse('Chau nos vemos en la proxima')

def mostraFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = '''<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>''' % fecha_actual

    return HttpResponse(documento)


def calculaEdad(request, edad, agno):

    #edadActual = 18
    periodo = agno - 2020
    edadFutura = edad + periodo
    documento = '<html><body><h2>En el año %s tendrás %s años</h2></body></html>' %(agno, edadFutura)

    return HttpResponse(documento)