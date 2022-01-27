from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.v1.store.views import CategoryViewSet, ProductViewSet
from api.v1.account.views import AccountViewSet, LocationViewSet

router = DefaultRouter()

router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"accounts", AccountViewSet, basename="accounts")
router.register(r"locations", LocationViewSet, basename="locations")


urlpatterns = [
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
