from rest_framework import viewsets
from .models import Pousada, Reserva
from .serializers import PousadaSerializer, ReservaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PousadaViewSet(viewsets.ModelViewSet):
    queryset = Pousada.objects.all().order_by('-criado')
    serializer_class = PousadaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tem_cafe','avaliacao']

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all().order_by('-criado')
    serializer_class = ReservaSerializer
