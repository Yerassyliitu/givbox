# Generated by Django 4.1.10 on 2023-11-30 10:35

import category.imggenerate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0014_modelextraservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=category.imggenerate.all_image_file_path, verbose_name='Фото'),
        ),
    ]
