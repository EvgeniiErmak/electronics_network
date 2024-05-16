# network/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    is_active_employee = models.BooleanField(_('Активный сотрудник'), default=False)


class NetworkNode(models.Model):
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )
    name = models.CharField(_('Название'), max_length=255)
    email = models.EmailField(_('Email'))
    country = models.CharField(_('Страна'), max_length=255)
    city = models.CharField(_('Город'), max_length=255)
    street = models.CharField(_('Улица'), max_length=255)
    house_number = models.CharField(_('Номер дома'), max_length=10)
    product_name = models.CharField(_('Название продукта'), max_length=255)
    product_model = models.CharField(_('Модель продукта'), max_length=255)
    product_release_date = models.DateField(_('Дата выхода продукта на рынок'))
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Поставщик'))
    debt = models.DecimalField(_('Задолженность'), max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _("Узел сети")
        verbose_name_plural = _("Узлы сети")

    def __str__(self):
        return self.name
