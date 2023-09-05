from django.contrib.auth.models import User

from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Aby hasło nie było widoczne w odpowiedzi
        }

    def create(self, validated_data):
        # Ta metoda pozwala na niestandardową obsługę tworzenia użytkownika
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user