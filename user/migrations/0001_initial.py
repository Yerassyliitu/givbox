# Generated by Django 4.1.10 on 2023-09-22 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('fullname', models.CharField(max_length=200, verbose_name='ФИО')),
                ('login', models.CharField(max_length=200, unique=True, verbose_name='Логин')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер телефона')),
                ('address', models.CharField(blank=True, max_length=256, null=True, verbose_name='Адресс')),
                ('avatar', models.TextField(blank=True, null=True, verbose_name='Ссылка на аватар')),
                ('user_type', models.CharField(choices=[('client', 'Клиент'), ('admin', 'Админ'), ('buyer', 'Покупатель'), ('depot_user', 'Склад'), ('support_user', 'Поддержка')], default='client', max_length=30, verbose_name='Тип пользователя')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModelWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя владельца')),
                ('currency', models.CharField(choices=[('som', 'сом'), ('ruble', 'рубль'), ('dollar', 'доллар')], default='som', max_length=10, verbose_name='Валюта')),
                ('amount', models.FloatField(default=0, verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Кошелек',
                'verbose_name_plural': 'Кошельки',
            },
        ),
        migrations.CreateModel(
            name='BuyerUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('passportNo', models.CharField(max_length=100, verbose_name='Номер пасспорта')),
                ('info', models.TextField(blank=True, verbose_name='Информация')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
            bases=('user.user',),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.modelcity', verbose_name='Город проживания')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.modelcountry', verbose_name='Страна проживания')),
                ('wallet', models.ManyToManyField(blank=True, to='user.modelwallet', verbose_name='Кошелек')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
            bases=('user.user',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности сотрудника')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
            bases=('user.user',),
        ),
        migrations.CreateModel(
            name='SupportUsers',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name='Номер пасспорта')),
            ],
            options={
                'verbose_name': 'Пользователь поддержки',
                'verbose_name_plural': 'Пользователи поддержки',
            },
            bases=('user.user',),
        ),
        migrations.CreateModel(
            name='ModelWalletHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('amount', models.FloatField(default=0, verbose_name='Сумма изменения')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'История изменении суммы кошелька',
                'verbose_name_plural': 'История изменении суммы кошелька',
            },
        ),
    ]
