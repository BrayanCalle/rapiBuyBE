from account.models import Location
from store.models import Order
from django.db import models


class Delivery (models.Model):
    """
    Person in charge of order delivery
    """
    first_name = models.CharField(max_length=250, verbose_name='Nombres')
    last_name = models.CharField(max_length=250, verbose_name='Apellidos')
    phone_number = models.CharField(verbose_name='Número de teléfono')
    email = models.EmailField(verbose_name='Correo electrónico')
    address = models.TextField(verbose_name='Dirección')
    identification_number = models.CharField(
        max_length=250, verbose_name='Número de identificación')
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='deliveries')


class Shipping (models.Model):
    ESTADO = (
        ('IN_PROGRESS', 'IN_PROGRESS'),
        ('SHIPPED', 'SHIPPED'),
        ('CANCELLED', 'CANCELLED'),
        ('REJECTED', 'REJECTED'),
    )
    delivery = models.ForeignKey(
        Delivery, on_delete=models.CASCADE, related_name='shippings')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='shippings')
    estado = models.CharField(
        max_length=50,
        choices=ESTADO,
        default='IN_PROGRESS',
        verbose_name='Estado'
    )
