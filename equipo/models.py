from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    color_camiseta = models.CharField(max_length=50)
    hinchada = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
