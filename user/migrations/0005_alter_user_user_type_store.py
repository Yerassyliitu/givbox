# Generated by Django 4.1.10 on 2023-10-26 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_category_storecategory_subcategory'),
        ('user', '0004_buyeruser_countries_buyeruser_websites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('client', 'Клиент'), ('admin', 'Админ'), ('buyer', 'Покупатель'), ('depot_user', 'Склад'), ('support_user', 'Поддержка'), ('store', 'Магазин')], default='client', max_length=30, verbose_name='Тип пользователя'),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Почта')),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('slogan', models.CharField(blank=True, max_length=200, null=True, verbose_name='Слоган')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('instagram', models.CharField(blank=True, max_length=200, null=True, verbose_name='Инстаграм')),
                ('facebook', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фейсбук')),
                ('whatsapp', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ватсап')),
                ('web', models.CharField(blank=True, max_length=200, null=True, verbose_name='Веб')),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('sale_type', models.CharField(choices=[('retail', 'розница'), ('wholesale', 'Оптом'), ('both', 'Оптом и розница')], default='retail', max_length=50, verbose_name='Тип продажи')),
                ('priority', models.FloatField(default=0, verbose_name='Приоритет')),
                ('rating', models.FloatField(default=5, verbose_name='Рейтинг')),
                ('visibility', models.BooleanField(default=True, verbose_name='Видимость')),
                ('cashback', models.FloatField(default=0, verbose_name='Кэш бэк')),
                ('storeCategory', models.ManyToManyField(to='category.storecategory', verbose_name='Категория магазина')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'ordering': ('-id',),
            },
            bases=('user.user',),
        ),
    ]
