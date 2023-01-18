from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    fono = models.CharField(max_length=10)
    email = models.CharField(max_length=150)
    estado_civil = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100,null=True)

class Marca(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self) :
        return self.nombre
    class Meta:
        db_table = 'marca'

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self) :
        return self.nombre
    class Meta:
        db_table = 'categoria'

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    descripcion = models.CharField(null = True,max_length=100)
    stock = models.IntegerField()
    estado = models.SmallIntegerField(default = 0)
    marca = models.ForeignKey(Marca,on_delete= models.RESTRICT)
    categoria = models.ForeignKey(Categoria,on_delete= models.RESTRICT)
    class Meta:
        db_table = 'producto'