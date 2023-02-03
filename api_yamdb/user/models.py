from django.db import models
from django.contrib.auth.models import AbstractUser

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
        max_length=254, #странное требование теста
        verbose_name='Email',
        help_text='Укажите email пользователя',
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография пользователя',
        help_text='Напишите биографию пользователя',
    )
    role = models.CharField(
        max_length=9,
        choices=Roles.choices,
        default=Roles.USER,
        verbose_name='Роль пользователя',
        help_text='Укажите роль пользователя',
    )
    first_name = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='Фамилия пользователя',
        max_length=150,
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    @property
    def is_admin(self):
        return self.is_staff or self.role == self.Roles.ADMIN    

    def __str__(self):
        return self.email

    @property
    def is_moderator(self):
        return self.role == self.Roles.MODERATOR
