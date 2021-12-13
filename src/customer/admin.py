"""
Admin
"""
from app.customer.models import Address, Customer
from django.contrib import admin

<<<<<<< HEAD
from customer.models import Address, Customer

=======
>>>>>>> 12fe739 (Configuring containers.)

# Register your models here.
class AddressInline(admin.TabularInline):
    """
    Inline Address
    """

    model = Address
    verbose_name = "Dirección"
    verbose_name_plural = "Direcciónes"
    fields = ("phone_number", "street", "city", "country", "postal_code")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "identification_number")
    search_fields = ("first_name", "last_name", "identification_number")
    list_filter = ("first_name", "last_name", "identification_number")
    fieldsets = (
        (
            ("Información de Cuenta"),
            {"fields": ("first_name", "last_name", "email", "identification_number", "user")},
        ),
    )
    inlines = (AddressInline,)


admin.site.register(Customer, CustomerAdmin)
