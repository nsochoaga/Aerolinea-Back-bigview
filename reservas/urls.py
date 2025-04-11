from django.urls import path
from .views import api_home, ListaVuelosView, ReservaView, CancelarReservaView, RegistroUsuarioView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('', api_home),
    path('auth/register/', RegistroUsuarioView.as_view(), name='registro-usuario'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('vuelos/', ListaVuelosView.as_view(), name='lista-vuelos'),
    path('reservas/', ReservaView.as_view(), name='reservas'),
    path('reservas/<int:pk>/', CancelarReservaView.as_view(), name='cancelar-reserva'),
]