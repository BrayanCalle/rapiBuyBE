from django.contrib import admin
from app.delivery.models import DeliveryMan, Vehicle, Shipping

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    """
    Vehicle Account
    """
    list_display = ("model", "plate", "vehicle_type")
    search_fields = ("model", "plate", "vehicle_type")
    list_filter = ("model", "plate", "vehicle_type")
    fieldsets = ((("Información del Vehículo"), {"fields": ("model", "plate", "license_plate", "year", "vehicle_type","delivery_man")}),)



class DeliveryManAdmin(admin.ModelAdmin):
    """
    Delivery Account
    """
    list_display = ("first_name", "last_name", "identification_number")
    search_fields = ("first_name", "last_name", "identification_number")
    list_filter = ("first_name", "last_name", "identification_number")
    fieldsets = ((("Información de Cuenta"), {"fields": ("first_name", "last_name", "email", "identification_number","account")}),)


admin.site.register(DeliveryMan, DeliveryManAdmin)
admin.site.register(Vehicle, VehicleAdmin)