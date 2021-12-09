"""
Models
"""
from django.db import models
from app.customer.models import Customer
from app.account.models import Account, Location


class Category(models.Model):
    """
    Category model, Clasificación de los diferentes productos.
    """

    name = models.CharField(max_length=80, verbose_name="Nombre")
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

    name = models.CharField(max_length=100, verbose_name="Nombre")
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
    Cart model, Contiene el detalle del carrito de compras.
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
    CartItem model, Producto o ítem que esta dentro del detalle del carrito de compras.
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
    Order model, Contiene el detalle de la orden.
    """

    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    tax_iva = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    shipping_fee = models.DecimalField(max_digits=12, decimal_places=2, default=0.0) #Gastos de envío
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name="order")


class OrderItem(models.Model):
    """
    OrderItem model, Producto o ítem que esta dentro del detalle de la orden.
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
