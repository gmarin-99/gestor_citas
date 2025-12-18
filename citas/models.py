from django.db import models
from django.contrib.auth.models import User

class Cita(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"
