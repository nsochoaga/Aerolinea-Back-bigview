from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, DestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from .models import Vuelo, Reserva
from .serializers import VueloSerializer, ReservaSerializer, UsuarioRegistroSerializer

User = get_user_model()

@api_view(["GET"])
def api_home(request):
    return Response({"message": "API de Aerolínea funcionando"})

class RegistroUsuarioView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioRegistroSerializer

class ListaVuelosView(ListAPIView):
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['origen', 'destino', 'fecha_salida']

class ReservaView(ListCreateAPIView):
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reserva.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class CancelarReservaView(DestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.usuario != self.request.user:
            raise PermissionDenied("No puedes cancelar una reserva que no es tuya.")
        instance.delete()