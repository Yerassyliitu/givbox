# Generated by Django 4.1.10 on 2023-09-29 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameKg', models.CharField(max_length=100, verbose_name='Кыргызча аталышы')),
                ('nameEn', models.CharField(max_length=100, verbose_name='Tariff name')),
                ('nameRu', models.CharField(max_length=100, verbose_name='Название')),
                ('icon', models.TextField(blank=True, verbose_name='Иконка')),
                ('extraCost', models.FloatField(default=0, verbose_name='Дополнительная стоимость')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='ModelCosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costPerKg', models.FloatField(default=0, verbose_name='Стоимость за kg')),
                ('costPerKgMy', models.FloatField(default=0, verbose_name='Стоимость за kg my')),
                ('costPerVW', models.FloatField(default=0, verbose_name='Стоимость за VW')),
                ('fromCity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_city', to='category.modelcity', verbose_name='Из города')),
                ('toCity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_city', to='category.modelcity', verbose_name='В город')),
            ],
            options={
                'verbose_name': 'Расход',
                'verbose_name_plural': 'Расходы',
            },
        ),
    ]
