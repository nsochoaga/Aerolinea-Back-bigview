from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Vuelo(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha_salida})"


class Usuario(AbstractUser):
    # Campos adicionales si se requieren
    pass

class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva de {self.usuario.username} para vuelo {self.vuelo.id}"