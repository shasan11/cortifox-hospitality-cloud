from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, UserBatchViewSet, AppUsersViewSet

router = DefaultRouter()
router.register(r'custom-users', CustomUserViewSet)
router.register(r'user-batches', UserBatchViewSet)
router.register(r'app-users', AppUsersViewSet)

urlpatterns = [
    path('users/', include(router.urls)),
]
