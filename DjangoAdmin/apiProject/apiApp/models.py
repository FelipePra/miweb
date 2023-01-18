from django.db import models

# Create your models here.

class Alumno(models.Model):
    matricula = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    fono= models.CharField(max_length=11)

    def __str__(self):
        return self.matricula
