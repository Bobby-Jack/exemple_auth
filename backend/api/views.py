

# Create your views here.
from rest_framework import generics

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.forms import AuthenticationForm
import json
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework_simplejwt.tokens import RefreshToken 
from django.http import JsonResponse # je pourrais envoyer des reponse en Json

from .models import Article, Profil
from .serializers import ArticleSerializer
from .forms import CustomUserCreationForm
from rest_framework_simplejwt.authentication import JWTAuthentication # Je vais gérer les token de manière simplifiée




@api_view(['GET'])
def ping(request):
    print("start ping")
    return Response({'message': 'ping succès.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register_user(request):
    print('register start')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            Profil.objects.create(user=user, role="viewer")
            return Response({'message': 'Utilisateur créé avec succès.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Méthode non autorisée.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def connexion(request):
    #idem que dans mon def inscription, comme j'ai pas de serializer, je vais décortiquer les données grace a Json.loads
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    print(username)
    print(password)
    user = authenticate(request, username=username, password=password) # ici au lieu de crée un user, j'utilise la fonction authenticate pour crée une instance du user connecté
    print(user)
    if user is not None:
    #si le user n'est pas égal a None (donc qu'il existe dans la db )    
        login(request, user)# j'utilise la fonction login
        refresh = RefreshToken.for_user(user)# génère un token de rafraichissement (on expliquera plus tard la différence entre token normal et refresh)
        access_token = str(refresh.access_token)# le principe du token access est qu'il est génèré a partir du refresh-token 
        # ensuite j'envois en réponseJson un message success et les tokens nécéssaire pour le header des requetes depuis le front
        return JsonResponse({'status': 'success', 'message': 'le user est connecté', 'access_token': access_token, 'refresh_token': str(refresh)})
    else:
        return JsonResponse({'status': 'error', 'message': "ptin smorch po lo"})
    
    


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]