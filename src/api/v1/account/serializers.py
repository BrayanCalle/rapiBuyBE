from rest_framework import serializers

from account.models import Account, Location


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        read_only_fields = [
            "id",
        ]
        fields = ["name", "acronym"] + read_only_fields

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        read_only_fields = [
            "id",
        ]
        fields = ["name", "street_address"] + read_only_fields