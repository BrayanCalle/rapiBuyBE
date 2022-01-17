from rest_framework import serializers

from store.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = [
            "id",
        ]
        fields = ["name", "description"] + read_only_fields
