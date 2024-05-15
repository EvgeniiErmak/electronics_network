# network/admin.py

from django.contrib import admin
from .models import CustomUser, NetworkNode
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Персональная информация'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Разрешения'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_active_employee')}),
        (_('Важные даты'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active_employee'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active_employee')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


@admin.action(description='Очистить задолженность у выбранных узлов')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'debt', 'supplier_link', 'created_at')
    list_filter = ('city',)
    search_fields = ('name',)
    actions = [clear_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="/admin/network/networknode/{}/change/">{}</a>', obj.supplier.id, obj.supplier.name)
        return '-'
    supplier_link.short_description = 'Поставщик'


admin.site.register(NetworkNode, NetworkNodeAdmin)
