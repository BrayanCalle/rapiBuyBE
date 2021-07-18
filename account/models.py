from django.contrib.auth.models import User
from django.db import models


class Account (models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    acronym = models.CharField(max_length=100, verbose_name='Sigla')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customers')


class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    phone_number = models.CharField(
        max_length=255, verbose_name='Numero de telefono')
    street_address = models.CharField(max_length=255, verbose_name='Direccion')
    email = models.EmailField(
        max_length=255, verbose_name='Correo electronico')
    city = models.CharField(max_length=255, verbose_name='Ciudad')
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='locations')
