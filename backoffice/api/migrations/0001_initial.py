# Generated by Django 3.2 on 2021-04-28 20:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                                        primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('balance', models.PositiveIntegerField(default=0, help_text='в копейках',
                                                        verbose_name='Баланс')),
                ('hold', models.PositiveIntegerField(default=0, verbose_name='Холд')),
                ('status', models.BooleanField(default=True, verbose_name='Открыт?')),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
