# Generated by Django 4.1.10 on 2024-01-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_modelitem_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelitem',
            name='descHtml',
            field=models.TextField(blank=True, verbose_name='Описание HTML'),
        ),
    ]
