from django.contrib.auth.models import User
from django.db import models


class Account (models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    acronym = models.CharField(max_length=100, verbose_name='Sigla')

    def __str__(self):
        return 'Name: {}'.format(self.name)


class AccountUser (models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='users')


class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    phone_number = models.CharField(
        max_length=255, verbose_name='Número de teléfono')
    street_address = models.CharField(max_length=255, verbose_name='Dirección')
    email = models.EmailField(
        max_length=255, verbose_name='Correo electrónico')
    city = models.CharField(max_length=255, verbose_name='Ciudad')
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return 'Name: {}'.format(self.name)
