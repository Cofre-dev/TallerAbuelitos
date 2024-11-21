from django.shortcuts import render
from django.http import HttpResponse
from .models import * #Llamando a los objetos del archivo Models

def test(request):
    return HttpResponse("Hola mundo")

def create(request):
    comment = Coments(name='Matías', score=6, coment ='Mi primer comentario') #Creando el objeto
    comment.save() #Comando para guardar los datos en la BD
    comment = Coments.objects.create(name="jose")
    return HttpResponse("Hola")

def delete(request):
    comment = Coments.objects.get(id=1) #Forma 1 para borrar un comentario
    comment.delete()
    Coments.objects.filter(id=2).delete()#Forma 2 para borrar un comentario
    return HttpResponse("Ruta para borrar los comentarios")


