import csv

from django.core.management.base import BaseCommand

from reviews.models import Category, Comment, Genre, Review, Title
from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):  # noqa: C901
        del options

        def load_category(**rows):
            return Category(**rows).save()

        for row in csv.DictReader(
            open('./static/data/category.csv', encoding='utf8'),
        ):
            load_category(id=row['id'], name=row['name'], slug=row['slug'])

        def load_genre(**rows):
            return Genre(**rows).save()

        for row in csv.DictReader(
            open('./static/data/genre.csv', encoding='utf8'),
        ):
            load_genre(id=row['id'], name=row['name'], slug=row['slug'])

        def load_user(**rows):
            return User(**rows).save()

        for row in csv.DictReader(
            open('./static/data/users.csv', encoding='utf8'),
        ):
            load_user(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name'],
            )

        def load_title(**rows):
            return Title(**rows).save()

        for row in csv.DictReader(
            open('./static/data/titles.csv', encoding='utf8'),
        ):
            load_title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category'],
            )

        def load_review(**rows):
            return Review(**rows).save()

        for row in csv.DictReader(
            open('./static/data/review.csv', encoding='utf8'),
        ):
            load_review(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author'],
                score=row['score'],
                pub_date=row['pub_date'],
            )

        def load_comment(**rows):
            return Comment(**rows).save()

        for row in csv.DictReader(
            open('./static/data/comments.csv', encoding='utf8'),
        ):
            load_comment(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date'],
            )
