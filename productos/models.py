from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    # CASCADE: Permite que si se elimina una categoria, se eliminen todos los productos asociados a ella.
    # PROTECT: Evita que se eliminen productos que están asociados a una categoria.
    # RESTRICT: Evita que se eliminen productos que están asociados a una categoria.
    # SET: Asigna un valor a la categoria del producto si se elimina la categoria.
    # SET_NULL: Asigna None a la categoria del producto si se elimina la categoria.
    # SET_DEFAULT: Asigna un valor por defecto a la categoria del producto si se elimina la categoria.
    # DO_NOTHING: No hace nada si se elimina la categoria.

    creado_en = models.DateTimeField(default=timezone.now)
