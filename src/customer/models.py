"""
Models"""

from django.db import models


class Customer(models.Model):
    """
    Customer model, Comprador u cliente
    """

    first_name = models.CharField(max_length=80, verbose_name="Nombres", null=True)
    last_name = models.CharField(max_length=80, verbose_name="Apellidos", null=True)
    email = models.EmailField(verbose_name="Correo electrónico")
    identification_number = models.CharField(
        max_length=10, verbose_name="Número de identificación", null=True
    )

    def __str__(self):
        return "{}".format(self.first_name)


class Address(models.Model):
    """
    Address model
    """

    phone_number = models.CharField(max_length=20, verbose_name="Número de teléfono")
    street = models.CharField(max_length=50, verbose_name="Calle Principal")
    city = models.CharField(max_length=50, verbose_name="Ciudad")
    country = models.CharField(max_length=50, verbose_name="País")
    postal_code = models.CharField(max_length=20, verbose_name="Código Postal")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
