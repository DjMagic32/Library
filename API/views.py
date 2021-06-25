from rest_framework import generics
from books.models import book
from .serializers import BookSerializers


# Create your views here.
class BookAPIView (generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializers

# En las líneas superiores, importamos la clase de vistas genéricas de Django REST Framework,

# los modelos de nuestra aplicación de libros y los serializadores de nuestra aplicación api

# (crearemos los serializadores a continuación).

# Luego, creamos un BookAPIView que usa ListAPIView para crear un 'endpoint' de solo lectura para todas las instancias de libros.

# Hay muchas vistas genéricas disponibles y las exploraremos con más detalle en capítulos posteriores.
