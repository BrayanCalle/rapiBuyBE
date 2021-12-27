"""
Models
"""
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.db import models
from django.db.models.deletion import PROTECT
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    """
    Account model de Empresa u Supermercado
    """

    name = models.CharField(max_length=80, verbose_name="Nombre")
    acronym = models.CharField(max_length=50, verbose_name="Sigla")

    def __str__(self):
        return "{}".format(self.name)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email is null")
        validator = EmailValidator()
        if validator(email):
            raise ValueError("Email invalid")
        if not kwargs.get("username"):
            raise ValueError("Username invalid")

        user = self.model(email=self.normalize_email(email), username=kwargs.get("username"))

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    account = models.ForeignKey(
        Account, null=True, blank=True, on_delete=PROTECT, related_name="users"
    )
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username


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
