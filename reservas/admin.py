from django.contrib import admin
from .models import Vuelo, Reserva, Usuario  # importa tus modelos

admin.site.register(Vuelo)
admin.site.register(Reserva)
admin.site.register(Usuario)