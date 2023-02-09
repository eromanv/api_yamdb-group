import re

from django.core.exceptions import ValidationError

from user.models import User


def validate_username(username):
    if username == 'me':
        raise ValidationError('Нельзя использовать "me" как имя пользователя')
    if not re.compile(r'[\w.@+-]+').fullmatch(username):
        restricted_symbols = re.compile(r'[\w.@+-]+').sub('', username)
        raise ValidationError(
            'Имя пользователя должно быть не более 150 символов, и '
            'состоять из букв, цифр и символов ./@/+/-/_.'
            f'Использование {restricted_symbols} недопоступимо.',
        )
    return username


def validate_email(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError('Такой адрес почты уже используется.')
    return email
