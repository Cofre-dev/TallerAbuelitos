#Dentro de una vista tenemos diferentes funciones que ejecutan la lógica 
from django.http import HttpResponse #type: ignore
from django.shortcuts import render #type: ignore

#Función principal de la web
def index(request):
    return render(request, 'index.html', {})
  
def herencia(request):
    return render(request, 'herencia.html', {})

def ejemplo(request):
    return render(request, 'ejemplo.html', {})

def otras(request):
    return render(request, 'otras.html', {})

def ejercicio(request):
    return render(request, 'ejercicio.html', {})

def portfolio(request):
    return render(request,'portfolio.html', {})