from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import Account, Location
from api.v1.account.serializers import (
    AccountSerializer,
    CategorySerializer,
    LocationSerializer,
    ProductSerializer,
)
from store.models import Category, Product


class AccountViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API
    """

    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ["name", "acronym"]
    ordering = ["name"]

    def get_queryset(self):
        return Account.objects.all()

    @action(detail=True, url_path="categories")
    def categories(self, request, *args, **kwargs):
        search = self.request.query_params.get("search")

        query = Category.objects.filter(account=self.get_object())

        if search:
            query = query.filter(name__icontains=search)

        response_serializer = CategorySerializer(query, many=True)

        return Response(response_serializer.data)

    @action(detail=True, url_path="products")
    def products(self, request, *args, **kwargs):
        search = self.request.query_params.get("search")
        category = self.request.query_params.get("category")

        query = Product.objects.filter(account=self.get_object())

        if search:
            query = query.filter(name__icontains=search)

        if category:
            query = query.filter(category__name__iexact=category)

        response_serializer = ProductSerializer(query, many=True)
        return Response(response_serializer.data)

    @action(detail=True, url_path="locations")
    def locations(self, request, *args, **kwargs):
        search = self.request.query_params.get("search")
        query = Location.objects.filter(account=self.get_object())

        if search:
            query = query.filter(name__icontains=search)

        response_serializer = LocationSerializer(query, many=True)
        return Response(response_serializer.data)
