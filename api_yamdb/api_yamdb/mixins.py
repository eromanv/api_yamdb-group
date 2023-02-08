from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.serializers import BaseSerializer

from .permissions import IsAdminOwnerModeratorOrReadOnly
from user.validators import validate_username, validate_email


class ListCreateDestroyViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    """Вьюсет для POST, GET и DELETE запросов.
    Поддерживает url с динамической переменной slug.
    """

    permission_classes = (IsAdminOwnerModeratorOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class UsernameSerializer(BaseSerializer):
    """Сериализатор для username."""

    def validate_username(self, username):
        return validate_username(username)

    def validate_email(self, email):
        return validate_email(email)
