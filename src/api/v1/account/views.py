from rest_framework import permissions, viewsets

from account.models import Account
from api.v1.account.serializers import AccountSerializer


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows coins to be viewed or edited.
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]
