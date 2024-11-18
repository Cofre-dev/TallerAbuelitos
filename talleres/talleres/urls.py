from django.contrib import admin  #type: ignore
from django.urls import path #type: ignore
from . import views


#Acá es donde escribimos las rutas y urls del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name='saludo'),
    path('despedida/', views.despedida, name='despedida'),
    path('adulto/<int:edad>/',views.adulto, name='adulto'), #Ejemplo de URL donde hay parametros <int:edad>
    path('simple/', views.simple, name='simple'),
    path('dinamico/<str:name>', views.dinamico, name='dinamico'),
]