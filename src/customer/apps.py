"""
Apps
"""
from django.apps import AppConfig


class CustomerConfig(AppConfig):
    """
    CustomerConfig
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "app.customer"
