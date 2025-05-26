# ¿Qué es un serializer?
# Convierte objetos Django (como modelos) en datos JSON y valida datos JSON entrantes 
# para crear/actualizar instancias.


from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    '''
    Este código define un serializador en DRF, una pieza fundamental para convertir datos complejos, 
    como instancias de modelos de Django, en formatos que puedan ser fácilmente renderizados a JSON, XML 
    o cualquier otro tipo de contenido, y viceversa.
    '''

    class Meta:
        model = Task  # Le indica al ModelSerializer que debe generar sus campos basándose en el modelo Task. DRF inspeccionará el modelo Task y creará automáticamente un campo de serializador para cada campo del modelo (por ejemplo, si Task tiene un CharField llamado title, el serializador creará un campo title correspondiente).
        fields = '__all__' #le dice al serializador que incluya todos los campos definidos en el modelo Task cuando serialice los datos. Si quisieras incluir solo campos específicos, podrías usar una tupla o lista, por ejemplo: fields = ['id', 'title', 'description', 'completed'].
        read_only_fields = ['owner'] # (Opción de seguridad) Evitamos que el cliente fije el owner manualmente
        
        # En este caso, owner se establece como read_only_field. Esto significa que cuando un cliente 
        # envía datos a tu API (por ejemplo, para crear o actualizar una tarea), no podrá especificar 
        # ni modificar el campo owner directamente.