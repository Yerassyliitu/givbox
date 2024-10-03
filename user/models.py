from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from category.models import ModelCountry, ModelCity, ModelWebsite, StoreCategory, ModelContact
from user import utils


class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, login, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not login:
            raise ValueError('User must have an Email or Phone')
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password):
        """create a superuser"""
        user = self.create_user(login, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Model for user"""
    fullname = models.CharField(max_length=200, verbose_name="ФИО")
    login = models.CharField(max_length=200, unique=True, verbose_name="Логин")
    phone = models.CharField('Номер телефона', max_length=50, null=True, blank=True)
    address = models.CharField('Адресс', max_length=256, null=True, blank=True)
    avatar = models.TextField('Ссылка на аватар', null=True, blank=True)
    user_type = models.CharField('Тип пользователя', choices=utils.USER_TYPE, default=utils.CLIENT, max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    reset_code = models.CharField(verbose_name='Код для сброса пароля', max_length=6, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'login'


class ModelWallet(models.Model):
    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'

    client_name = models.CharField('Имя владельца', null=True, blank=True, max_length=100)
    currency = models.CharField('Валюта', choices=utils.WALLET_CURRENCY, default=utils.SOM, max_length=10)
    amount = models.FloatField('Сумма', default=0)


class Client(User):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    country = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True, verbose_name='Страна проживания')
    city = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True, verbose_name='Город проживания')
    dateCreated = models.DateTimeField('Дата регистрации', auto_now_add=True, blank=True, null=True)
    wallet = models.ManyToManyField(ModelWallet, blank=True, verbose_name='Кошелек')
    passport_front = models.TextField('Лицевая сторона паспорта', blank=True)
    passport_back = models.TextField('Обратная сторона паспорта', blank=True)
    isVerified = models.BooleanField('Проверено', default=False)
    inn = models.CharField('INN', max_length=200, blank=True, null=True)
    isVip = models.BooleanField('Статус VIP', default=False)

    def __str__(self):
        return str(self.fullname)


class Employee(User):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    active = models.BooleanField('Статус активности сотрудника', default=True)

    def __str__(self):
        return str(self.fullname)


class ModelWalletHistory(models.Model):
    class Meta:
        verbose_name = 'История изменении суммы кошелька'
        verbose_name_plural = 'История изменении суммы кошелька'

    date = models.DateTimeField('Дата и время', auto_now_add=True)
    amount = models.FloatField('Сумма изменения', default=0)
    client = models.ForeignKey(Client, models.SET_NULL, null=True, blank=True, verbose_name='Клиент')
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return str(self.client.fullname)


class BuyerUser(User):
    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    passportNo = models.CharField('Номер пасспорта', max_length=100)
    info = models.TextField('Информация', blank=True)
    countries = models.ManyToManyField(ModelCountry, blank=True, verbose_name='Страны', related_name='countries')
    websites = models.ManyToManyField(ModelWebsite, blank=True, verbose_name='Веб сайты')
    passport_front = models.TextField('Лицевая сторона пасспорта', blank=True)
    passport_back = models.TextField('Обратная сторона пасспорта', blank=True)
    experience = models.TextField('Опыт работы', blank=True)
    commission = models.TextField('Размер комиссии', blank=True)
    paymentType = models.CharField('Способ оплаты', max_length=100, null=True, blank=True)
    search_product = models.TextField('Поиск товаров', blank=True)
    contacts = models.ForeignKey(ModelContact, models.SET_NULL, null=True, blank=True, verbose_name='Контакты')
    country = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True, verbose_name='Страна',
                                related_name='country_foreignKey')
    redemption_speed = models.CharField('Скорость погашения', max_length=100, null=True, blank=True)
    email = models.EmailField('Электронная почта', null=True, blank=True)
    insta = models.TextField('Инстаграм', blank=True)
    instaLink = models.TextField('Ссылка на инстаграм', blank=True)
    face = models.TextField('Фейсбук', blank=True)
    faceLink = models.TextField('Ссылка на фейсбук', blank=True)
    tg = models.TextField('Телеграм', blank=True)
    tgLink = models.TextField('Ссылка на телеграм', blank=True)
    whatsApp = models.TextField('Whatsapp', blank=True)
    whatsAppLink = models.TextField('Ссылка на WhatsApp', blank=True)

    def __str__(self):
        return str(self.fullname)

    def clean(self):
        self.user_type = utils.BUYER


class SupportUsers(User):
    class Meta:
        verbose_name = 'Пользователь поддержки'
        verbose_name_plural = 'Пользователи поддержки'

    dateCreated = models.DateTimeField('Номер пасспорта', auto_now_add=True)

    def __str__(self):
        return str(self.fullname)

    def clean(self):
        self.user_type = utils.SUPPORT_USER


class Store(User):
    """Model for user"""
    class Meta:
        ordering = ('-id',)
        verbose_name = ("Магазин")
        verbose_name_plural = ("Магазины")

    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name="Почта")
    location = models.CharField(max_length=200, null=True, blank=True)
    slogan = models.CharField(max_length=200, null=True, blank=True, verbose_name="Слоган")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    instagram = models.CharField(max_length=200, null=True, blank=True, verbose_name="Инстаграм")
    facebook = models.CharField(max_length=200, null=True, blank=True, verbose_name="Фейсбук")
    whatsapp = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ватсап")
    web = models.CharField(max_length=200, null=True, blank=True, verbose_name="Веб")
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    storeCategory = models.ManyToManyField(StoreCategory, verbose_name="Категория магазина")
    sale_type = models.CharField(choices=utils.SALE_TYPE, default=utils.RETAIL, verbose_name='Тип продажи', max_length=50)
    priority = models.FloatField(default=0, verbose_name="Приоритет")
    rating = models.FloatField(default=5, verbose_name="Рейтинг")
    visibility = models.BooleanField(verbose_name="Видимость", default=True)
    cashback = models.FloatField(verbose_name='Кэш бэк', default=0)

    def save(self, *args, **kwargs):
        super(Store, self).save(*args, **kwargs)
        self.user_type = utils.STORE


class ModelBecomeBuyer(models.Model):
    class Meta:
        verbose_name = 'Стать покупателем'
        verbose_name_plural = 'Стать покупателем'

    client = models.ForeignKey(Client, models.CASCADE, verbose_name='Клиент')
    passport_front = models.TextField('Лицевая сторона пасспорта', blank=True)
    passport_back = models.TextField('Обратная сторона пасспорта', blank=True)
    comment = models.TextField('Комментарий', blank=True)
    accepted = models.BooleanField('Принял', default=False)
    dateCreated = models.DateTimeField('Дата создания', auto_now_add=True)
    fullname = models.CharField('ФИО', max_length=200, blank=True)
    about_yourself = models.TextField('О себе', blank=True)
    experience = models.TextField('Опыт работы', blank=True)
    commission = models.TextField('Размер комиссии', blank=True)
    redemption_speed = models.CharField('Скорость выкупа', max_length=200)
    country = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True, verbose_name='Страна проживания',
                                related_name='live_country')
    shop_countries = models.ManyToManyField(ModelCountry, blank=True, related_name='shop_countries')
    paymentType = models.CharField('Способ оплаты', max_length=100, null=True, blank=True)
    search_product = models.TextField('Поиск товаров', blank=True)
    rating = models.FloatField('Рейтинг', default=0)
    contacts = models.ForeignKey(ModelContact, models.SET_NULL, null=True, blank=True, verbose_name='Контакты')
    redemption_speed = models.CharField('Скорость погашения', max_length=100, null=True, blank=True)
    email = models.EmailField('Электронная почта', null=True, blank=True)
    insta = models.TextField('Инстаграм', blank=True)
    instaLink = models.TextField('Ссылка на инстаграм', blank=True)
    face = models.TextField('Фейсбук', blank=True)
    faceLink = models.TextField('Ссылка на фейсбук', blank=True)
    tg = models.TextField('Телеграм', blank=True)
    tgLink = models.TextField('Ссылка на телеграм', blank=True)
    whatsApp = models.TextField('Whatsapp', blank=True)
    whatsAppLink = models.TextField('Ссылка на WhatsApp', blank=True)

    def __str__(self):
        return str(self.client.fullname)


class ModelShopUser(User):
    class Meta:
        verbose_name = 'Клиент магазина'
        verbose_name_plural = 'Клиенты магазина'

    dateRegistered = models.DateTimeField('Дата регистрации', auto_now_add=True)

    def save(self, *args, **kwargs):
        super(ModelShopUser, self).save(*args, **kwargs)
        self.user_type = utils.SHOP_USER


class ConfirmEmailModel(models.Model):
    class Meta:
        verbose_name = 'Подтвержденная почта'
        verbose_name_plural = 'Подтвержденные почты'

    email = models.CharField('Электронная почта', max_length=250)
    confirm_code = models.CharField(verbose_name='Код для подтверждения электронной почты', max_length=6, blank=True)

    def __str__(self):
        return str(self.email)
