# Generated by Django 4.1.10 on 2023-10-26 07:03

import category.imggenerate
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_user_type_store'),
        ('category', '0010_alter_subcategory_category'),
        ('core', '0012_modelbuyerrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание товара')),
                ('cost', models.FloatField(default=0, verbose_name='Цена товара')),
                ('issale', models.BooleanField(default=False, verbose_name='Акционный товар?')),
                ('costSale', models.FloatField(default=0, verbose_name='Акционная цена товара')),
                ('uniqueid', models.CharField(blank=True, max_length=200, null=True, verbose_name='Штрихкод')),
                ('image', models.ImageField(blank=True, null=True, upload_to=category.imggenerate.all_image_file_path, verbose_name='Фото')),
                ('imagelink', models.TextField(blank=True, null=True, verbose_name='Линк фото товара')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Телефон номер')),
                ('instagram', models.CharField(blank=True, max_length=200, null=True, verbose_name='Инстаграм')),
                ('facebook', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фейсбук')),
                ('whatsapp', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ватсап')),
                ('web', models.CharField(blank=True, max_length=200, null=True, verbose_name='Веб')),
                ('likes', models.IntegerField(default=0, verbose_name='Число лайков')),
                ('views', models.IntegerField(default=0, verbose_name='Число просмотров')),
                ('sale_type', models.CharField(choices=[('retail', 'розница'), ('wholesale', 'Оптом'), ('both', 'Оптом и розница')], default='retail', max_length=50, verbose_name='Тип продажи')),
                ('isoptovik', models.BooleanField(default=False, verbose_name='Оптовый товар')),
                ('optovikcost', models.FloatField(default=0, verbose_name='Оптовая цена товара')),
                ('priority', models.FloatField(default=0, verbose_name='Приоритет')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category', verbose_name='Категория товара')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.subcategory', verbose_name='Сабкатегория товара')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.store', verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
