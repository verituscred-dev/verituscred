from django.db import models
from cloudinary.models import CloudinaryField

class Documento(models.Model):
    nome = models.CharField(max_length=100)
    arquivo = CloudinaryField('documentos/')  # Armazena no Cloudinary automaticamente

class CalculoRevisional(models.Model):
    nome = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    email = models.EmailField()
    valor_total = models.CharField(max_length=100, blank=True)
    qtd_parcelas = models.IntegerField(blank=True, null=True)
    parcelas_pagas = models.IntegerField(blank=True, null=True)
    valor_parcela = models.CharField(max_length=100, blank=True)
    mensagem = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class SimulacaoEmprestimo(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    situacao_profissional = models.CharField(max_length=50)
    valor_total = models.CharField(max_length=30)
    renda_mensal = models.CharField(max_length=30)
    mensagem = models.TextField(blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"
