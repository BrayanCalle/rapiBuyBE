"""
models
"""
from django.db import models

from account.models import Account
from store.models import Order


class DeliveryMan(models.Model):
    """
    Person in charge of order delivery
    Persona encargada de la entrega del pedido
    """

    first_name = models.CharField(max_length=80, verbose_name="Nombres")
    last_name = models.CharField(max_length=80, verbose_name="Apellidos")
    phone_number = models.CharField(max_length=15, verbose_name=" Número de teléfono")
    email = models.EmailField(verbose_name="Correo electrónico")
    address = models.TextField(verbose_name="Dirección")
    identification_number = models.CharField(max_length=10, verbose_name="Número de identificación")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="deliveries")

    def __str__(self):
        return "{}".format(self.first_name)


class Vehicle(models.Model):
    """
    Transporte de repartidor
    """

    TYPE = (("CAR", "CAR"), ("MOTORCYCLE", "MOTORCYCLE"))
    model = models.CharField(max_length=80, verbose_name="Modelo")
    plate = models.CharField(max_length=20, null=True, verbose_name="Placa")
    license_plate = models.CharField(max_length=100, null=True, verbose_name="Nombres")
    year = models.PositiveIntegerField(default=0)
    vehicle_type = models.CharField(
        max_length=50, choices=TYPE, default="CAR", verbose_name="Vehículo"
    )
    delivery_man = models.ForeignKey(DeliveryMan, on_delete=models.CASCADE, related_name="vehicles")


class Shipping(models.Model):
    """
    Detalle de envio
    """

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
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="shippings")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="shippings")
    estado = models.CharField(
        max_length=50, choices=ESTADO, default="IN_PROGRESS", verbose_name="Estado"
    )
