from rest_framework import serializers
from books.models import book


class BookSerializers (serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ('title', 'subtitle', 'author', 'isbn')

# En las líneas superiores, importamos la clase de serializadores de Django REST Framework y el modelo de libro de nuestra aplicación de libros.

# Extendemos ModelSerializer de Django REST Framework a una clase BookSerializer que especifica nuestro modelo de base de datos Book

# y los campos de la base de datos que deseamos exponer: título, subtítulo, autor e isbn.

# ¡Eso es! Hemos terminado.
