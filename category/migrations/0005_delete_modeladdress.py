# Generated by Django 4.1.10 on 2023-10-16 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_client_addresses'),
        ('category', '0004_modeladdress'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ModelAddress',
        ),
    ]
