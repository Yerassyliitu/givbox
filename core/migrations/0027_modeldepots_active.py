# Generated by Django 4.1.10 on 2023-12-13 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_cartrequest_modelbuyerrequest_cart_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeldepots',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Статус активности'),
        ),
    ]
