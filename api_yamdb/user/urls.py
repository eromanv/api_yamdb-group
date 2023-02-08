from django.urls import include, path
from rest_framework.routers import DefaultRouter

from user.views import AuthViewSet, UserTokenViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

authpatterns = [
    path('signup/', AuthViewSet.as_view()),
    path('token/', UserTokenViewSet.as_view()),
]

urlpatterns = [
    path('auth/', include(authpatterns)),
    path('', include(router.urls)),
]
