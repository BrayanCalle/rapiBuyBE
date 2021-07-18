from account.models import Account, Location
from django.contrib.auth.models import User
from django.db import models


class Customer (models.Model):
    first_name = models.CharField(max_length=250, verbose_name='Nombres')
    last_name = models.CharField(max_length=250, verbose_name='Apellidos')
    phone_number = models.CharField(verbose_name='Numero de telefono')
    email = models.EmailField(verbose_name='Correo electronico')
    address = models.TextField(verbose_name='Direccion')
    identification_number = models.CharField(
        max_length=250, verbose_name='Numero de identificacion')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customers')


class Category (models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(
        upload_to='storage/category', null=True, default=None)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='categories')


class Product(models.Model):
    """
    Contiene los datos de un producto que se manejan dentro de una empresa
    """
    name = models.CharField(max_length=255, verbose_name='Nombre')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad', default=0)
    image = models.ImageField(
        upload_to='storage/products', null=True, default=None)
    price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name='Precio', default=0.0)
    tax = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name='Iva', default=0.0)
    description = models.TextField(
        verbose_name='Descripción', null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return '{} Precio: {}'.format(self.name, self.price)


class Cart (models.Model):
    subtotal = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    discount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='carts')
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='carts')


class CartItem (models.Model):
    quantity = models.PositiveIntegerField(verbose_name='Cantidad', default=0)
    unit_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    discount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='items')


class Order (models.Model):
    subtotal = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    discount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    cart = models.OneToOneField(
        Cart, on_delete=models.CASCADE, related_name='order')


class OrderItem (models.Model):
    quantity = models.PositiveIntegerField(verbose_name='Cantidad', default=0)
    unit_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    discount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    cart_item = models.OneToOneField(
        CartItem, on_delete=models.CASCADE, related_name='items')
