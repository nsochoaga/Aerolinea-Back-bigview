from rest_framework import serializers
from .models import Vuelo, Reserva
from django.contrib.auth import get_user_model


User = get_user_model()

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    vuelo = VueloSerializer(read_only=True)
    vueloId = serializers.PrimaryKeyRelatedField(
        queryset=Vuelo.objects.all(), write_only=True, source="vuelo"
    )
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Reserva
        fields = ['id', 'fecha_reserva', 'usuario', 'vuelo', 'vueloId']
