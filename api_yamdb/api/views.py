from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets
from rest_framework.pagination import PageNumberPagination

from api.serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleReadSerializer,
    TitleWriteSerializer,
)
from api_yamdb.mixins import ListCreateDestroyViewSet
from api_yamdb.permissions import (
    IsAdminOwnerModeratorOrReadOnly,
    IsAdminUserOrReadOnly,
)
from reviews.filters import TitleFilter
from reviews.models import Category, Genre, Review, Title


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(Avg('reviews__score'))
    serializer_class = TitleWriteSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminOwnerModeratorOrReadOnly,)

    def get_queryset(self):
        title = generics.get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'),
        )
        return title.reviews.select_related('author').all()

    def perform_create(self, serializer):
        title = generics.get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'),
        )
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminOwnerModeratorOrReadOnly,)

    def get_queryset(self):
        review = generics.get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
        )
        return review.comments.select_related('author').all()

    def perform_create(self, serializer):
        review = generics.get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
        )
        serializer.save(author=self.request.user, review=review)
