from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User


class AuthSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(max_length=150)
    email = serializers.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email', 'username')

    def validate(self, data):
        if User.objects.filter(
            username=data['username'],
            email=data['email'],
        ).exists():
            return data
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError(
                'Пользователь с таким именем существует.',
            )
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError(
                'Пользователь с таким email существует.',
            )
        if data['username'] == 'me':
            raise serializers.ValidationError(
                'Использовать имя "me" в качестве username запрещено.',
            )
        return data


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField(max_length=150)


class UserSerializer(serializers.ModelSerializer):
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
    role = serializers.ChoiceField(
        choices=['user', 'moderator', 'admin'],
        default='user',
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
