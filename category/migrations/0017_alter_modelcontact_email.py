# Generated by Django 4.1.10 on 2023-12-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0016_modelcontact_messangers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcontact',
            name='email',
            field=models.EmailField(max_length=256, verbose_name='Электронная почта'),
        ),
    ]
