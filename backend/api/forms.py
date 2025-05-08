from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Assurez-vous d'importer votre modèle personnalisé

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',) # Exemple: ajouter le champ email


