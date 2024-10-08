# Generated by Django 4.1.10 on 2023-11-09 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_client_datecreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyeruser',
            name='passport_back',
            field=models.TextField(blank=True, verbose_name='Обратная сторона пасспорта'),
        ),
        migrations.AddField(
            model_name='buyeruser',
            name='passport_front',
            field=models.TextField(blank=True, verbose_name='Лицевая сторона пасспорта'),
        ),
        migrations.CreateModel(
            name='ModelBecomeBuyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_front', models.TextField(blank=True, verbose_name='Лицевая сторона пасспорта')),
                ('passport_back', models.TextField(blank=True, verbose_name='Обратная сторона пасспорта')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('accepted', models.BooleanField(default=False, verbose_name='Принял')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Стать покупателем',
                'verbose_name_plural': 'Стать покупателем',
            },
        ),
    ]
