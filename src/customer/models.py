"""
Models"""

from django.db import models
# from account.models import UserNuevo

# class Customer(models.Model):
#     """
#     Customer model, Comprador u cliente
#     """

#     first_name = models.CharField(max_length=80, verbose_name="Nombres", null=True, blank=True)
#     last_name = models.CharField(max_length=80, verbose_name="Apellidos", null=True, blank=True)
#     email = models.EmailField(verbose_name="Correo electrónico", unique=True)
#     identification_number = models.CharField(
#         max_length=10, verbose_name="Número de identificación", null=True, blank=True
#     )

#     def __str__(self):
#         return "{}".format(self.first_name)

class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    identification_number = models.CharField(
        max_length=10, verbose_name="Número de identificación", unique=True
    )
    first_name = models.CharField(max_length=80, verbose_name="Nombres")
    last_name = models.CharField(max_length=80, verbose_name="Apellidos")
    # phone_number = models.CharField(max_length=20, verbose_name="Número de teléfono")
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

# ----------------------------------------------------


# from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class Customer(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='Correo electrónico',
#         max_length=50,
#         unique=True,
#     )
#     first_name = models.CharField(max_length=80, verbose_name="Nombres", null=True)
#     last_name = models.CharField(max_length=80, verbose_name="Apellidos", null=True)
#     identification_number = models.CharField(
#         max_length=10, verbose_name="Número de identificación", null=True
#     )
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `rapiBuy`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin

# class Address(models.Model):
#     """
#     Address model
#     """

#     phone_number = models.CharField(max_length=20, verbose_name="Número de teléfono")
#     street = models.CharField(max_length=50, verbose_name="Calle Principal")
#     city = models.CharField(max_length=50, verbose_name="Ciudad")
#     country = models.CharField(max_length=50, verbose_name="País")
#     postal_code = models.CharField(max_length=20, verbose_name="Código Postal")
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
