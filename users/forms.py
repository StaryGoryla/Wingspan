from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreation(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'is_online']