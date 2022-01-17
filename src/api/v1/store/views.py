from rest_framework import mixins, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from pagination import CustomPagination
from store.models import Category, Product

from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = [
        "name",
    ]
    ordering = ["name"]
    search_fields = ["name", "account__acronym"]

    @property
    def user(self):
        return self.request.user

    def get_queryset(self):
        return Category.objects.filter(account=self.user.account)


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ["created_at", "name", "price"]
    ordering = ["-created_at"]
    search_fields = ["name", "category__id", "account__acronym"]

    def get_queryset(self):
        return Product.objects.all()
