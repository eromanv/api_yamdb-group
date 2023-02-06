from django.urls import include, path
from rest_framework.routers import DefaultRouter

from user.views import AuthViewSet, UserTokenViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('auth/signup/', AuthViewSet.as_view()),
    path('auth/token/', UserTokenViewSet.as_view()),
    path('', include(router.urls)),
]
