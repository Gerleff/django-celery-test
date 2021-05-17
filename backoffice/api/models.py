"""Апи-модели"""
from uuid import uuid4

from django.db import models


class Account(models.Model):
    """Модель счета"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    full_name = models.CharField('ФИО', max_length=255)
    balance = models.PositiveIntegerField('Баланс', help_text='в копейках', default=0)
    hold = models.PositiveIntegerField('Холд', default=0)
    status = models.BooleanField('Открыт?', default=True)

    class Meta:
        """Настройки отображения и хранения в базе"""
        db_table = 'accounts'

    @staticmethod
    def prettify_money(money):
        """Для красивого вывода балансов"""
        if type(money) == int:
            return f'{money // 100} rub {money % 100} cop'
        return money

    def to_dict(self) -> dict:
        """Словарное представление модели с учетом хранения валюты в копейках"""
        acc_dict = {a: self.prettify_money(self.__dict__[a])
                    for a in self.__dict__ if a != '_state'}
        return acc_dict

    def __str__(self):
        """Строковое представление в админке и ORM"""
        return self.full_name
