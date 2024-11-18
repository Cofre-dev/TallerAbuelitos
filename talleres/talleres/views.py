#Dentro de una vista tenemos diferentes funciones que ejecutan la lógica 
from django.http import HttpResponse #type: ignore
from django.shortcuts import render #type: ignore

#Función que saluda
def saludo(request):
    return HttpResponse("Hola mundo") 

#Función que se despide
def despedida(request):
    return HttpResponse("Adios mundo")

#Una función con un poco más de lógica
def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("No eres mayor de edad")

def simple(request):
    return render(request, 'simple.html',{})


def dinamico(request, name):
    categories = ['code', 'desing', 'marketing']
    context = {'name' : name, 'categories' : categories}
    return render(request, 'dinamico.html', context)

