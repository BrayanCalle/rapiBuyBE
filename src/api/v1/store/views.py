from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from pagination import CustomPagination
from store.models import Category

from .serializers import CategorySerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    @property
    def user(self):
        return self.request.user

    def get_queryset(self):
        return Category.objects.filter(account=self.user.account)
