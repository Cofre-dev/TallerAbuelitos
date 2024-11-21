from django.db import models
from datetime import *
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Entry(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #realizando la conexión entre llaves foraneas 
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    public_date = models.DateField(default=date.today)
    reating = models.IntegerField(default=5)
    
    def __str__(self):
        return self.headline
    
    