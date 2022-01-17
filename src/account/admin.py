"""
admin
"""
from django.contrib import admin

from account.models import Account, Location, User


class LocationInline(admin.TabularInline):
    """
    Inline location
    """

    model = Location
    verbose_name = "Local"
    verbose_name_plural = "Locales"
    fields = ("name", "phone_number", "street_address", "email", "city")


class AccountAdmin(admin.ModelAdmin):
    """
    Admin Account
    """

    list_display = ("name", "acronym")
    search_fields = ("name", "acronym")
    list_filter = ("name", "acronym")
    fieldsets = ((("Información de Cuenta"), {"fields": ("name", "acronym")}),)
    inlines = (LocationInline,)


admin.site.register(Account, AccountAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
