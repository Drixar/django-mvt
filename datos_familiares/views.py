from math import remainder
from urllib import request
from django.shortcuts import render
from datos_familiares.models import Familia
import datetime
from django.http import HttpResponse, response
# Create your views here.

def inicio(request):
    return render(request, "index.html")

def ver_familiares(request):
    familiares = Familia.objects.all()
    datos = {"datos" : familiares}
    return render(request, "ver_familiares.html", datos)

def alta_familiares(request):
    familiar = Familia(nombre= "Mariana", fechaDeNacimiento= "1968-04-17", dni= 20123456)
    familiar.save()
    familiar = Familia(nombre= "Ana", fechaDeNacimiento= "1998-07-04", dni= 41234567)
    familiar.save()
    familiar = Familia(nombre= "Florencia", fechaDeNacimiento= "1999-09-12", dni= 42234567)
    familiar.save()
    return HttpResponse("Registros creados correctamente")