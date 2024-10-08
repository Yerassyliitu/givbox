# Generated by Django 4.1.13 on 2024-10-03 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_cartrequest_itemcost_cartrequest_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelrequests',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Приватный'),
        ),
        migrations.AddField(
            model_name='modelrequests',
            name='private_item_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание приватного товара'),
        ),
        migrations.AddField(
            model_name='modelrequests',
            name='product_link',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка на товар'),
        ),
    ]
