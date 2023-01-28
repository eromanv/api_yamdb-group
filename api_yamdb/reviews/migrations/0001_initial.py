# Generated by Django 3.2 on 2023-01-28 15:50

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import reviews.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'password',
                    models.CharField(max_length=128, verbose_name='password'),
                ),
                (
                    'last_login',
                    models.DateTimeField(
                        blank=True, null=True, verbose_name='last login'
                    ),
                ),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text='Designates that this user has all permissions without explicitly assigning them.',
                        verbose_name='superuser status',
                    ),
                ),
                (
                    'is_staff',
                    models.BooleanField(
                        default=False,
                        help_text='Designates whether the user can log into this admin site.',
                        verbose_name='staff status',
                    ),
                ),
                (
                    'is_active',
                    models.BooleanField(
                        default=True,
                        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                        verbose_name='active',
                    ),
                ),
                (
                    'date_joined',
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name='date joined',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        max_length=254,
                        unique=True,
                        verbose_name='Адрес электронной почты',
                    ),
                ),
                (
                    'username',
                    models.CharField(
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name='Имя пользователя (nickname)',
                    ),
                ),
                (
                    'first_name',
                    models.CharField(
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name='Имя пользователя',
                    ),
                ),
                (
                    'last_name',
                    models.CharField(
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name='Фамилия пользователя',
                    ),
                ),
                (
                    'role',
                    models.CharField(
                        choices=[
                            ('admin', 'Administrator'),
                            ('moderator', 'Moderator'),
                            ('user', 'User'),
                        ],
                        default='user',
                        max_length=50,
                        verbose_name='Вид доступа',
                    ),
                ),
                (
                    'bio',
                    models.TextField(
                        blank=True, null=True, verbose_name='О себе'
                    ),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.Group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.Permission',
                        verbose_name='user permissions',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=256, verbose_name='Название категории'
                    ),
                ),
                (
                    'slug',
                    models.SlugField(
                        unique=True, verbose_name='Идентификатор категории'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=256, verbose_name='Название жанра'
                    ),
                ),
                (
                    'slug',
                    models.SlugField(
                        unique=True, verbose_name='Идентификатор жанра'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=256, verbose_name='Название произведения'
                    ),
                ),
                (
                    'year',
                    models.IntegerField(
                        validators=[reviews.validators.validate_year],
                        verbose_name='Год',
                    ),
                ),
                (
                    'description',
                    models.TextField(
                        blank=True, null=True, verbose_name='Описание'
                    ),
                ),
                (
                    'category',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='title',
                        to='reviews.category',
                        verbose_name='Категория произведения',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ('-year',),
            },
        ),
        migrations.CreateModel(
            name='TitleGenre',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'genre',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='reviews.genre',
                        verbose_name='Жанр произведения',
                    ),
                ),
                (
                    'title',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='reviews.title',
                        verbose_name='Произведение',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Произведение с жанром',
                'verbose_name_plural': 'Произведения с жанрами',
            },
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(
                through='reviews.TitleGenre',
                to='reviews.Genre',
                verbose_name='Жанр',
            ),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('text', models.TextField()),
                (
                    'score',
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                (
                    'pub_date',
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reviews',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'title',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reviews',
                        to='reviews.title',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('text', models.TextField()),
                (
                    'pub_date',
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'review',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        to='reviews.review',
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.CheckConstraint(
                check=models.Q(_negated=True, username__iexact='me'),
                name='username_is_not_me',
            ),
        ),
    ]
