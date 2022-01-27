from rest_framework import status
from rest_framework.exceptions import APIException


class ProductException(APIException):
    """Raised when the zendesk service has issues"""

    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "Error al buscar un producto, intente  mas tarde"
    default_code = "service_unavailable"
