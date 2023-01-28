from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import (UserViewSet, get_jwt_token,
                    register, CategoryViewSet, GenreViewSet, 
                    TitleViewSet)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]