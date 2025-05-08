

# Create your views here.
from rest_framework import generics

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .models import Article, Profil
from .serializers import ArticleSerializer
from .forms import CustomUserCreationForm



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