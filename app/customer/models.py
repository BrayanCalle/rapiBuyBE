"""
Models
"""
from django.db import models
from django.contrib.auth import get_user_model


class Customer(models.Model):
    """
    Customer model, Comprador u cliente
    """

    first_name = models.CharField(max_length=250, verbose_name="Nombres")
    last_name = models.CharField(max_length=250, verbose_name="Apellidos")
    email = models.EmailField(verbose_name="Correo electrónico")
    identification_number = models.CharField(
        max_length=250, verbose_name="Número de identificación"
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.first_name)

class Address(models.Model):
    """
    Address model
    """

    phone_number = models.CharField(max_length=250, verbose_name="Número de teléfono")
    street = models.CharField(max_length=250, verbose_name="Calle Principal")
    city = models.CharField(max_length=250, verbose_name="Ciudad")
    country = models.CharField(max_length=250, verbose_name="País")
    postal_code = models.CharField(max_length=250, verbose_name="Código Postal")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
