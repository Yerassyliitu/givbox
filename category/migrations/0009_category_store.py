# Generated by Django 4.1.10 on 2023-10-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_user_type_store'),
        ('category', '0008_category_storecategory_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='store',
            field=models.ManyToManyField(blank=True, to='user.store', verbose_name='Магазин'),
        ),
    ]
