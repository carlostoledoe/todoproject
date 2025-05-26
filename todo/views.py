from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

'''
¿Qué es un ViewSet?
Un ViewSet maneja las vistas para CRUD automáticamente. Se combina con un router para 
generar las URLs sin escribirlas manualmente.
'''

class TaskViewSet(viewsets.ModelViewSet): # Aquí definimos nuestra clase TaskViewSet. Al heredar de viewsets.ModelViewSet, estamos obteniendo una gran cantidad de funcionalidad "gratis" y automáticamente. Un ModelViewSet proporciona implementaciones para las operaciones CRUD (Crear, Leer, Actualizar, Borrar) para un modelo específico. 
    serializer_class = TaskSerializer # Esta línea le dice al ViewSet qué serializador debe usar para convertir las instancias del modelo Task a formatos de API (como JSON) y para validar los datos de entrada. En este caso, es nuestro TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # permission_classes define una lista de clases de permisos que se aplicarán a todas las acciones de este ViewSet. permissions.IsAuthenticated es una de las clases de permiso más comunes en DRF. Significa que solo los usuarios autenticados (es decir, aquellos que han iniciado sesión o han proporcionado un token válido) podrán acceder a cualquiera de las operaciones de este TaskViewSet. Si un usuario no autenticado intenta acceder, recibirá un error de "Autenticación fallida".

    def get_queryset(self): # Un queryset es el conjunto de objetos que el ViewSet debería considerar para sus operaciones de listado o detalle.
        # Cada usuario solo ve sus propias tareas
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer): # Cuando un cliente envía datos para crear una nueva tarea, el serializer ya ha validado esos datos (gracias a TaskSerializer).
        # Asigna automáticamente el owner al usuario autenticado
        serializer.save(owner=self.request.user)