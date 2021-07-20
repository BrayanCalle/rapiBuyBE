from account.models import Account
from django.db import models
from store.models import Order


class DeliveryMan(models.Model):
    """
    Person in charge of order delivery
    """

    first_name = models.CharField(max_length=250, verbose_name="Nombres")
    last_name = models.CharField(max_length=250, verbose_name="Apellidos")
    phone_number = models.CharField(max_length=250, verbose_name="Número de teléfono")
    email = models.EmailField(verbose_name="Correo electrónico")
    address = models.TextField(verbose_name="Dirección")
    identification_number = models.CharField(
        max_length=250, verbose_name="Número de identificación"
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="deliveries"
    )


class Vehicle(models.Model):
    TYPE = (("CAR", "CAR"), ("MOTORCYCLE", "MOTORCYCLE"))
    model = models.CharField(max_length=250, verbose_name="Modelo")
    plate = models.CharField(max_length=250, null=True, verbose_name="Placa")
    license_plate = models.CharField(max_length=250, null=True, verbose_name="Nombres")
    year = models.PositiveIntegerField(default=0)
    vehicle_type = models.CharField(
        max_length=50, choices=TYPE, default="CAR", verbose_name="Vehículo"
    )
    delivery_man = models.ForeignKey(
        DeliveryMan, on_delete=models.CASCADE, related_name="vehicles"
    )


class Shipping(models.Model):
    ESTADO = (
        ("IN_PROGRESS", "IN_PROGRESS"),
        ("SHIPPED", "SHIPPED"),
        ("CANCELLED", "CANCELLED"),
        ("REJECTED", "REJECTED"),
    )
    shipped_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)
    shipping_address = models.CharField(max_length=250)
    distance = models.PositiveIntegerField(default=0)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="shippings"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="shippings")
    estado = models.CharField(
        max_length=50, choices=ESTADO, default="IN_PROGRESS", verbose_name="Estado"
    )
