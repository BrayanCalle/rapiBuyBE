"""
admin
"""
import os

from django.contrib import admin
from store.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin Category
    """

    list_display = ("name", "image", "description", "account")
    search_fields = ("name", "description", "account")
    list_filter = ("name", "description", "account")
    fieldsets = (
        (("Datos Básicos"), {"fields": ("account", "name", "image", "description")}),
    )

    def save_model(self, request, obj, form, change):
        try:
            if obj.id:
                old_img = obj.__class__.objects.get(id=obj.id).image.path
                try:
                    new_img = obj.image.path
                except ValueError:
                    new_img = None

                if old_img != new_img:

                    if os.path.exists(old_img):
                        os.remove(old_img)
            obj.save()
        except ValueError:
            pass


class ProductAdmin(admin.ModelAdmin):
    """
    Admin Product
    """

    list_display = ("name", "image", "quantity", "price", "category", "description")
    search_fields = ("name", "description", "category")
    list_filter = ("name", "description", "category")
    fieldsets = (
        (
            ("Datos Básicos"),
            {
                "fields": (
                    "category",
                    "name",
                    "image",
                    "quantity",
                    "price",
                    "tax_iva",
                    "description",
                )
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        try:
            if obj.id:
                old_img = obj.__class__.objects.get(id=obj.id).image.path
                try:
                    new_img = obj.image.path
                except ValueError:
                    new_img = None

                if old_img != new_img:

                    if os.path.exists(old_img):
                        os.remove(old_img)
            obj.save()
        except ValueError:
            pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
