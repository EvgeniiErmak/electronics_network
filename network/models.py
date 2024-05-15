# network/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_active_employee = models.BooleanField(default=False)


class NetworkNode(models.Model):
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    product_name = models.CharField(max_length=255)
    product_model = models.CharField(max_length=255)
    product_release_date = models.DateField()
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Network Node"
        verbose_name_plural = "Network Nodes"

    def __str__(self):
        return self.name
