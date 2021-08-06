from api.account.serializers import AccountSerializer
from app.account.models import Account

from rest_framework import permissions, viewsets


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows coins to be viewed or edited.
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]
