from rest_framework import serializers

from account.models import Account, Location
from store.models import Category, Product


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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = [
            "id",
        ]
        fields = ["name", "description"] + read_only_fields


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = [
            "id",
        ]
        fields = ["name", "quantity", "price"] + read_only_fields
