from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # ✅ IMPORTANDO CloudinaryField

class Boleto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('pendente', 'Pendente'), ('pago', 'Pago')],
        default='pendente'
    )
    arquivo = CloudinaryField('arquivo', folder='boletos/', resource_type='auto')  # 📂 UPLOAD PARA CLOUDINARY

    def __str__(self):
        return f"Boleto de R$ {self.valor} - Vencimento: {self.data_vencimento}"

def processar_boletos():
    from boletos.models import Boleto  # Importação dentro da função
    boletos = Boleto.objects.all()
    for boleto in boletos:
        print(boleto)
