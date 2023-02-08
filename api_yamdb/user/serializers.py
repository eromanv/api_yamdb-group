from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User
from api_yamdb.mixins import UsernameSerializer


class AuthSerializer(serializers.ModelSerializer, UsernameSerializer):
    username = serializers.SlugField(max_length=150)
    email = serializers.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email', 'username')


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField(max_length=150)


class UserSerializer(serializers.ModelSerializer, UsernameSerializer):
    username = serializers.RegexField(
        max_length=150,
        regex=r'^[\w.@+-]+\Z',
        validators=[
            UniqueValidator(queryset=User.objects.all()),
        ],
    )
    email = serializers.EmailField(
        max_length=254,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
        ],
    )

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
