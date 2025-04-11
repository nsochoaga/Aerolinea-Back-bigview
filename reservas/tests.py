from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Vuelo, Reserva
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class APITests(APITestCase):

    def setUp(self):
        # Crear usuario
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.vuelo = Vuelo.objects.create(
            origen="Bogotá",
            destino="Medellín",
            fecha_salida="2025-05-01",
            hora_salida="08:00",
            capacidad=100
        )

    def test_listar_vuelos(self):
        url = reverse('lista-vuelos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_crear_reserva_autenticado(self):
        user = User.objects.create_user(username='usuario_test', password='testpass')
        # Generar token JWT
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        url = reverse('reservas')
        data = {"vuelo": self.vuelo.id}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_crear_reserva_no_autenticado(self):
        url = reverse('reservas')
        data = {"vuelo": self.vuelo.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)