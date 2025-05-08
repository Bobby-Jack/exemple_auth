
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Profil, CustomUser # Imp
class Command(BaseCommand):
    help = 'Crée un compte administrateur et son profil si inexistant.'

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(is_superuser=True).exists():
            user = CustomUser.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='adminpassword'  # Changez ceci dans un environnement réel !
            )
            Profil.objects.create(user=user, role='admin')  # Crée le profil admin
            self.stdout.write(self.style.SUCCESS('Compte administrateur et son profil créés avec succès.'))
        else:
            self.stdout.write(self.style.SUCCESS('Le compte administrateur et son profil existent déjà.'))