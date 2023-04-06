from rest_framework.routers import DefaultRouter

from apps.users.api.api import UserViewSet

router = DefaultRouter()

router.register("users", UserViewSet, basename = "users")

urlpatterns = router.urls