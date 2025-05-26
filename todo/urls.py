from rest_framework.routers import DefaultRouter # Esta línea importa la clase DefaultRouter de DRF. Los "Routers" (enrutadores) son una característica muy poderosa de DRF que automatizan la generación de URLs para tus ViewSets. Esto te ahorra una enorme cantidad de código repetitivo al definir todas las rutas CRUD para tu TaskViewSet.
from .views import TaskViewSet
from django.urls import path, include

router = DefaultRouter() # Aquí creamos una instancia de DefaultRouter. Este objeto será el encargado de gestionar las URLs que se generarán automáticamente.
router.register(r'tasks', TaskViewSet, basename='task')

# router.register(): Este método le dice al router que genere un conjunto de URLs para un ViewSet específico.
# /tasks/ (para listar o crear tareas)
# /tasks/{id}/ (para obtener, actualizar o borrar una tarea específica) La r antes de la cadena indica una "raw string" (cadena cruda), lo cual es una buena práctica para expresiones regulares.
# TaskViewSet: Le estamos indicando al router que este prefijo (tasks) debe mapearse a las acciones (list, create, retrieve, update, destroy) definidas en tu TaskViewSet.
# basename='task': Este argumento es opcional, pero muy recomendado. Le da un nombre base al conjunto de URLs generadas. DRF lo usa para generar nombres de URL únicos y para propósitos de ingeniería inversa (por ejemplo, reverse('task-list') o reverse('task-detail', args=[task.id])). Si no lo proporcionas, DRF intentará inferir un nombre de tu ViewSet, pero es mejor ser explícito

urlpatterns = [
    path('', include(router.urls)), # include(router.urls): Aquí es donde las URLs generadas por el DefaultRouter se "inyectan" en tus urlpatterns. El router.urls es una lista de objetos URL que el router ha creado.
]

'''
DefaultRouter generará automáticamente las siguientes URLs para ti:

GET /tasks/: Lista de tareas (mapeado a TaskViewSet.list())
POST /tasks/: Crear una nueva tarea (mapeado a TaskViewSet.create())
GET /tasks/{pk}/: Detalle de una tarea específica (mapeado a TaskViewSet.retrieve())
PUT /tasks/{pk}/: Actualizar completamente una tarea (mapeado a TaskViewSet.update())
PATCH /tasks/{pk}/: Actualizar parcialmente una tarea (mapeado a TaskViewSet.partial_update())
DELETE /tasks/{pk}/: Borrar una tarea (mapeado a TaskViewSet.destroy())
'''