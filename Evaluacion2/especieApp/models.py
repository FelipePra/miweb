from django.db import models

# Create your models here.

class Especie(models.Model):
    especie = models.CharField(max_length=100)