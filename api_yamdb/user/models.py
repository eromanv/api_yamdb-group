from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin'
        MODERATOR = 'moderator'
        USER = 'user'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    email = models.EmailField(
        db_index=True,
        unique=True,
        max_length=254,
        help_text='Укажите email пользователя',
    )
    bio = models.TextField(
        blank=True,
        verbose_name='биография',
        help_text='Напишите биографию пользователя',
    )
    role = models.CharField(
        max_length=9,
        choices=Roles.choices,
        default=Roles.USER,
        verbose_name='роль',
        help_text='Выберите роль (администратор/модератор/пользователь)',
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=150,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=150,
        null=True,
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.is_staff or self.role == self.Roles.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.Roles.MODERATOR
