from django.contrib import admin

from api_yamdb.admin import BaseAdmin
from reviews.models import Category, Comment, Genre, Review, Title, TitleGenre


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = (
        'name',
        'slug',
    )
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Genre)
class GenreAdmin(BaseAdmin):
    list_display = (
        'name',
        'slug',
    )
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(TitleGenre)
class TitleGenreAdmin(BaseAdmin):
    list_display = (
        'title',
        'genre',
    )
    search_fields = (
        'title',
        'genre',
    )
    list_filter = (
        'title',
        'genre',
    )


@admin.register(Title)
class TitleAdmin(BaseAdmin):
    list_display = (
        'name',
        'year',
        'category',
        'description',
    )
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Comment)
class CommentAdmin(BaseAdmin):
    list_display = (
        'text',
        'review',
        'author',
        'pub_date',
    )
    search_fields = ('review',)
    list_filter = ('review',)


@admin.register(Review)
class ReviewAdmin(BaseAdmin):
    list_display = (
        'text',
        'title',
        'author',
        'score',
        'pub_date',
    )
    search_fields = ('pub_date',)
    list_filter = ('pub_date',)
