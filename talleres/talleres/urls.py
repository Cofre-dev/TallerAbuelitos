from django.contrib import admin  #type: ignore
from django.urls import path #type: ignore
from . import views


#Acá es donde escribimos las rutas y urls del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #Directorio raiz
    path('herencia/', views.herencia, name='herencia'),
    path('ejemplo', views.ejemplo, name='ejemplo'),
    path('otras', views.otras, name='otras'),
    path('ejercicio', views.ejercicio, name='ejercicio'),
    path('portfolio', views.portfolio, name='portfolio'),
]