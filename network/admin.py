# network/admin.py

from django.contrib import admin
from .models import CustomUser, NetworkNode
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_active_employee')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
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


@admin.action(description='Clear debt for selected nodes')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name',)
    actions = [clear_debt]


admin.site.register(NetworkNode, NetworkNodeAdmin)
