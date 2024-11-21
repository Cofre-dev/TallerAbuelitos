from django.db import models
import datetime

# Create your models here.
# Cada modelo es una clase que posteriormente será una tabla en la BD
#Cada vez que hagamos una modefificación en el archivo de modelos hay que actualizar la BD

class Coments(models.Model):
    
    #Modelando los datos
    name = models.CharField(max_length=250, null=False)
    score = models.IntegerField(default=3)
    coment = models.TextField(max_length=1500, null=True)
    date = models.DateField(null= True)
    signature = models.CharField(max_length=100, default="Firma")
            
    def __str__(self):
        return self.name


