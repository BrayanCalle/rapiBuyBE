from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from account.models import Account, Location
from api.v1.account.serializers import AccountSerializer, LocationSerializer


class AccountViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API
    """
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    ordering_fields = [
        "name","acronym"]
    ordering = ["name"]

    def get_queryset(self):
        return Account.objects.all()

class LocationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)
    ordering_fields = [
        "name","street_address"]
    ordering = ["name"]

    def get_queryset(self):
        return Location.objects.all()