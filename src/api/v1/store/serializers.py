from rest_framework import serializers

from store.models import Category, Product


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
