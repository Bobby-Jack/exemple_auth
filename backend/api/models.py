from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
class Profil(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('editor', 'Éditeur'),
        ('viewer', 'Lecteur'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    def __str__(self):
        return self.user.username

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
