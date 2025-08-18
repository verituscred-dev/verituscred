from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username

class Documento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="documentos")
    titulo = models.CharField(max_length=255, blank=True, null=True)  # Adicionando o campo título
    arquivo = CloudinaryField('arquivo', folder='documentos/', resource_type='auto')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    enviado_pelo_cliente = models.BooleanField(default=False)  # Indica se foi enviado pelo cliente
    arquivo = CloudinaryField('documentos/')

def __str__(self):
        tipo = "Cliente" if self.enviado_pelo_cliente else "Admin"
        return f"Documento de {self.usuario.username} ({tipo}) - {self.get_status_display()}"

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
