from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email') # Inclure les champs que vous voulez afficher

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True) # Affiche les informations de l'auteur

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at') # Ces champs ne peuvent pas être modifiés lors de la création/mise à jour