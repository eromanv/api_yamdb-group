from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from user.models import User


class NameSlugModel(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='идентификатор',
        max_length=50,
        unique=True,
    )

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genre(NameSlugModel):
    class Meta(NameSlugModel.Meta):
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class Category(NameSlugModel):
    class Meta(NameSlugModel.Meta):
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='название произведения',
    )
    year = models.IntegerField(
        verbose_name='Год',
        validators=(MaxValueValidator(timezone.now().year),),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='категория произведения',
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='жанр',
        through='TitleGenre',
    )

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'произведения'
        default_related_name = 'titles'
        ordering = ('name',)

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='произведение',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='жанр произведения',
    )

    class Meta:
        verbose_name = 'through-модель'
        verbose_name_plural = 'through-модели'

    def __str__(self):
        return f'{self.title}, жанр — {self.genre}'


class AuthorTextModel(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ('pub_date',)

    def __str__(self):
        return self.text


class Review(AuthorTextModel):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='произведение',
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='оценка',
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        default_related_name = 'reviews'
        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_author_title_in_review',
            ),
        ]


class Comment(AuthorTextModel):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='отзыв',
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        default_related_name = 'comments'
