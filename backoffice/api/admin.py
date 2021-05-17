"""Админка для апи-моделей"""
from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Описание админки счета"""
    readonly_fields = ('id', )
    list_display = ['id', 'full_name', 'balance', 'hold', 'status']
    search_fields = ['id', 'full_name']
    list_filter = ['status']
