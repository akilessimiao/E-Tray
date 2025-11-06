from rest_framework import serializers
from .models import Pousada, Reserva
class PousadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pousada
        fields = '__all__'
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
