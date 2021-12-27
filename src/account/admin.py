"""
admin
"""
from django.contrib import admin

from account.forms import UserForm
from account.models import Account, Location, User


class LocationInline(admin.TabularInline):
    """
    Inline location
    """

    model = Location
    verbose_name = "Local"
    verbose_name_plural = "Locales"
    fields = ("name", "phone_number", "street_address", "email", "city")


class UserInline(admin.TabularInline):
    """
    Inline User
    """

    model = User
    verbose_name = "Usuario"
    verbose_name_plural = "Usuarios"
    fields = ("user",)
    form = UserForm


class AccountAdmin(admin.ModelAdmin):
    """
    Admin Account
    """

    list_display = ("name", "acronym")
    search_fields = ("name", "acronym")
    list_filter = ("name", "acronym")
    fieldsets = ((("Información de Cuenta"), {"fields": ("name", "acronym")}),)
    inlines = (LocationInline, UserInline)


admin.site.register(Account, AccountAdmin)
