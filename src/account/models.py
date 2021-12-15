"""
Models
"""
from django.contrib.auth import get_user_model
from django.db import models


class Account(models.Model):
    """
    Account model de Empresa u Supermercado
    """

    name = models.CharField(max_length=80, verbose_name="Nombre")
    acronym = models.CharField(max_length=50, verbose_name="Sigla")

    def __str__(self):
        return "{}".format(self.name)


class AccountUser(models.Model):
    """
    Account user model, Persona o Usuario encargado de la cuenta de la Empresa
    """

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="users")


class Location(models.Model):
    """
    Location model u sucursal
    """

    name = models.CharField(max_length=100, verbose_name="Nombre")
    phone_number = models.CharField(max_length=15, verbose_name="Número de teléfono")
    street_address = models.CharField(max_length=100, verbose_name="Dirección")
    email = models.EmailField(max_length=80, verbose_name="Correo electrónico")
    city = models.CharField(max_length=30, verbose_name="Ciudad")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="locations")

    def __str__(self):
        return "Name: {}".format(self.name)
