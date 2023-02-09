from rest_framework import serializers

from api_yamdb.mixins import UsernameSerializer
from user.models import User


class AuthSerializer(serializers.Serializer, UsernameSerializer):
    username = serializers.SlugField(max_length=150)
    email = serializers.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email', 'username')


class TokenSerializer(serializers.Serializer, UsernameSerializer):
    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField(max_length=150)


class UserSerializer(serializers.ModelSerializer, UsernameSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
