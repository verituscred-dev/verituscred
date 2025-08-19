from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Cria um superusuário automaticamente se ele não existir"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "Verituscred")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "contato@verituscred.com.br")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Veritus.2025")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superusuário {username} criado com sucesso!"))
        else:
            self.stdout.write(self.style.WARNING(f"Superusuário {username} já existe."))
 
