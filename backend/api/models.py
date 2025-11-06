from django.db import models
class Pousada(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300, blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    avaliacao = models.FloatField(null=True, blank=True)
    tem_cafe = models.BooleanField(default=True)
    link = models.URLField(blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class Reserva(models.Model):
    pousada = models.ForeignKey(Pousada, on_delete=models.CASCADE)
    nome_hospede = models.CharField(max_length=150)
    checkin = models.DateField()
    checkout = models.DateField()
    criado = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Reserva {self.nome_hospede} - {self.pousada.nome}"
