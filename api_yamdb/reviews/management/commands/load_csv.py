import csv

from django.core.management.base import BaseCommand

from reviews.models import Category, Comment, Genre, Review, Title
from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        for row in csv.DictReader(
            open('./static/data/category.csv', encoding='utf8'),
        ):
            Category(id=row['id'], name=row['name'], slug=row['slug']).save()

        for row in csv.DictReader(
            open('./static/data/genre.csv', encoding='utf8'),
        ):
            Genre(id=row['id'], name=row['name'], slug=row['slug']).save()

        for row in csv.DictReader(
            open('./static/data/users.csv', encoding='utf8'),
        ):
            User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name'],
            ).save()

        for row in csv.DictReader(
            open('./static/data/titles.csv', encoding='utf8'),
        ):
            Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category'],
            ).save()

        for row in csv.DictReader(
            open('./static/data/review.csv', encoding='utf8'),
        ):
            Review(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author'],
                score=row['score'],
                pub_date=row['pub_date'],
            ).save()

        for row in csv.DictReader(
            open('./static/data/comments.csv', encoding='utf8'),
        ):
            Comment(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date'],
            ).save()
