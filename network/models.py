# network/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    is_active_employee = models.BooleanField(_('Активный сотрудник'), default=False)


class Contact(models.Model):
    email = models.EmailField(_('Email'))
    country = models.CharField(_('Страна'), max_length=255)
    city = models.CharField(_('Город'), max_length=255)
    street = models.CharField(_('Улица'), max_length=255)
    house_number = models.CharField(_('Номер дома'), max_length=10)

    class Meta:
        verbose_name = _("Контакт")
        verbose_name_plural = _("Контакты")

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house_number}"


class Product(models.Model):
    name = models.CharField(_('Название продукта'), max_length=255)
    model = models.CharField(_('Модель продукта'), max_length=255)
    release_date = models.DateField(_('Дата выхода продукта на рынок'))

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")

    def __str__(self):
        return f"{self.name} ({self.model})"


class NetworkNode(models.Model):
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )
    name = models.CharField(_('Название'), max_length=255)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name=_('Контакт'))
    products = models.ManyToManyField(Product, verbose_name=_('Продукты'))
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Поставщик'))
    debt = models.DecimalField(_('Задолженность'), max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _("Узел сети")
        verbose_name_plural = _("Узлы сети")

    def __str__(self):
        return self.name
