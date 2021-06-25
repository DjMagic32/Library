from django.urls import path
from .views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
]


# De la forma en que funciona Django, ahora cuando un usuario va a la página de inicio de nuestro sitio web,
# primero accederá al archivo library_project / urls.py,
# luego será redirigido a books / urls.py que especifica el uso de BookListView.
# En este archivo de vista, el modelo Libro se usa junto con ListView para enumerar todos los libros.

# El paso final es crear nuestro archivo de plantilla que controla el diseño en la página web real.
# Ya hemos especificado su nombre como book_list.html en nuestra vista.
#
# Hay dos opciones para su ubicación: por defecto,
# el cargador de plantillas de Django buscará plantillas dentro de nuestra
# aplicación de libros en la siguiente ubicación:
# books / templates / books / book_list.html.
#
# En su lugar, también podríamos crear un directorio de plantillas a nivel de proyecto
# separado y actualizar nuestro archivo settings.py para que apunte allí.
#
# Cuál usará en última instancia en sus propios proyectos es una preferencia personal.
# Usaremos la estructura predeterminada aquí.
# Si tiene curiosidad sobre el segundo enfoque, consulte el libro Django para principiantes.
# Comience creando una nueva carpeta de plantillas dentro de la aplicación de books,
# luego dentro de ella una carpeta de books y finalmente un archivo book_list.html.
