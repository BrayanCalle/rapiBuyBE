"""
admin
"""
from django.contrib import admin


class CategoriaAdmin(admin.ModelAdmin):
    """
    Administracion de categoria
    """

    list_display = ("name", "description")
    search_fields = ("name", "description")
    list_filter = ("name", "description")
    fieldsets = ((("Información de Categoría"), {"fields": ("name", "description")}),)
