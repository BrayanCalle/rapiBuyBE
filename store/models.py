"""
Models
"""
from django.db import models
from django.contrib.auth import get_user_model
from account.models import Account, Location


class Customer(models.Model):
    """
    Customer model
    """

    first_name = models.CharField(max_length=250, verbose_name="Nombres")
    last_name = models.CharField(max_length=250, verbose_name="Apellidos")
    phone_number = models.CharField(max_length=250, verbose_name="Número de teléfono")
    email = models.EmailField(verbose_name="Correo electrónico")
    address = models.TextField(verbose_name="Dirección")
    identification_number = models.CharField(
        max_length=250, verbose_name="Número de identificación"
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Category(models.Model):
    """
    Category model
    """

    name = models.CharField(max_length=250, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    image = models.ImageField(upload_to="storage/category", null=True, default=None)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self):
        return "{}-{}".format(self.name, self.account)


class Product(models.Model):
    """
    Contiene los datos de un producto que se manejan dentro de un negocio
    """

    name = models.CharField(max_length=255, verbose_name="Nombre")
    quantity = models.PositiveIntegerField(verbose_name="Cantidad", default=0)
    image = models.ImageField(upload_to="storage/products", null=True, default=None)
    price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Precio", default=0.0
    )
    tax_iva = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Iva", default=0.0
    )
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return "{} Price: {}".format(self.name, self.price)


class Cart(models.Model):
    """
    Cart model
    """

    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    tax_iva = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="carts"
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="carts"
    )


class CartItem(models.Model):
    """
    CartItem model
    """

    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    tax_iva = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")


class Order(models.Model):
    """
    Order model
    """

    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    tax_iva = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    shipping_fee = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name="order")


class OrderItem(models.Model):
    """
    OrderItem model
    """

    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    tax_iva = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    cart_item = models.OneToOneField(
        CartItem, on_delete=models.CASCADE, related_name="items"
    )
