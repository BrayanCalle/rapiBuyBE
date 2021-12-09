"""
admin
"""
from django.contrib import admin

from account.forms import AccountUserForm
from account.models import Account, AccountUser, Location


class LocationInline(admin.TabularInline):
    """
    Inline location
    """

    model = Location
    verbose_name = "Local"
    verbose_name_plural = "Locales"
    fields = ("name", "phone_number", "street_address", "email", "city")


class AccountUserInline(admin.TabularInline):
    """
    Inline User
    """

    model = AccountUser
    verbose_name = "Usuario"
    verbose_name_plural = "Usuarios"
    fields = ("user",)
    form = AccountUserForm


class AccountAdmin(admin.ModelAdmin):
    """
    Admin Account
    """

    list_display = ("name", "acronym")
    search_fields = ("name", "acronym")
    list_filter = ("name", "acronym")
    fieldsets = ((("Información de Cuenta"), {"fields": ("name", "acronym")}),)
    inlines = (LocationInline, AccountUserInline)


admin.site.register(Account, AccountAdmin)
