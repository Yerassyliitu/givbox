from email.policy import default

from django.contrib.postgres.fields import ArrayField
from django.db import models

from category import imggenerate
from category.models import ModelCountry, ModelCity, ModelWH, ModelContact, ModelPackageType, ModelTariff, Category, \
    SubCategory, ModelExtraService, ModelColor, ModelMemory, ModelMatrix, ModelNotification
from core import utils
from core.utils import PAYMENT_TYPE_CHOICES, PAYMENT_STATUS_CHOICES, CRYPTO_PAID, UNPAID
from user.models import Client, User, Store, ModelWallet
from user.utils import DEPOT_USER, SALE_TYPE, RETAIL


class ModelDepots(models.Model):
    class Meta:
        verbose_name = 'Депо'
        verbose_name_plural = 'Депо'

    nameKg = models.CharField('Депонун аталышы', max_length=100)
    nameEn = models.CharField('Depot\'s name', max_length=100)
    nameRu = models.CharField('Название Депо', max_length=100)
    infoRu = models.TextField('Информация на русском', blank=True)
    infoEn = models.TextField('Information', blank=True)
    infoKg = models.TextField('Маалымат', blank=True)
    address = models.CharField('Адресс', max_length=256, null=True, blank=True)
    maxAmount = models.FloatField('Максимальное количество', default=0)
    country = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True, verbose_name='Страна')
    city = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True, verbose_name='Город')
    workingHours = models.ManyToManyField(ModelWH, blank=True, verbose_name='Режим роботы')
    contacts = models.ForeignKey(ModelContact, models.SET_NULL, null=True, blank=True, verbose_name='Контакты')
    images = ArrayField(models.TextField(), null=True, blank=True, verbose_name='Рисунки')
    lat = models.FloatField('LAT', default=0)
    lon = models.FloatField('LON', default=0)
    types = models.CharField('Тип депо', max_length=10, choices=utils.DEPOT_TYPE, default=utils.BOTH)
    extraServices = models.ManyToManyField(ModelExtraService, blank=True, verbose_name='Экстра сервисы')
    isCommercial = models.BooleanField('Коммерческий', default=False)
    active = models.BooleanField('Статус активности', default=True)
    video = models.TextField('Видео', blank=True)
    cityStr = models.TextField('City', blank=True)
    instructionsRu = models.TextField('Инструкция', blank=True)
    instructionsKg = models.TextField('Корсотмолор', blank=True)
    instructionsEn = models.TextField('Instructions', blank=True)
    link_zip = models.TextField('Ccылка на ZIP', blank=True)
    nameStr = models.TextField('Название', blank=True)
    nameStart = models.BooleanField('Name start', default=False)
    stateStr = models.TextField('State str', blank=True)
    surnameStr = models.CharField('Surname', max_length=250, blank=True)
    email = models.CharField('Email', max_length=250, blank=True)

    def __str__(self):
        return str(self.nameRu)


class TariffSchedule(models.Model):
    class Meta:
        verbose_name = 'Тарифная сетка'
        verbose_name_plural = 'Тарифные сетки'
    depot = models.OneToOneField(ModelDepots, on_delete=models.CASCADE, related_name='tariff_schedule')

    def __str__(self):
        return self.depot.nameRu


class TariffList(models.Model):
    schedule = models.ForeignKey(TariffSchedule, on_delete=models.CASCADE, related_name='tariff')
    weight = models.DecimalField('Вес в кг.', max_digits=10, decimal_places=1)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)


class ModelPackageData(models.Model):
    class Meta:
        verbose_name = 'Информация о пакете'
        verbose_name_plural = 'Информации о пакетах'

    nameKg = models.CharField('Кыргызча аталышы', max_length=100)
    nameEn = models.CharField('Package data name', max_length=100)
    nameRu = models.CharField('Название', max_length=100)
    infoRu = models.TextField('Информация', blank=True)
    infoKg = models.TextField('Маалымат', blank=True)
    infoEn = models.TextField('Information', blank=True)
    height = models.FloatField('Высота', default=0)
    length = models.FloatField('Длина', default=0)
    width = models.FloatField('Ширина', default=0)
    weight = models.FloatField('Вес', default=0)
    order = models.IntegerField(default=10)
    icon = models.TextField('Иконка', blank=True)


class ModelItem(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    name = models.CharField(max_length=500, verbose_name="Название товара")
    description = models.TextField(null=True, blank=True, verbose_name="Описание товара")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория товара")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name="Сабкатегория товара")
    cost = models.FloatField(default=0, verbose_name="Цена товара")
    issale = models.BooleanField(default=False, verbose_name="Акционный товар?")
    costSale = models.FloatField(default=0, verbose_name="Акционная цена товара")
    supplier = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Магазин")
    uniqueid = models.CharField(max_length=200, null=True, blank=True, verbose_name="Штрихкод")
    image = models.FileField(null=True, blank=True, upload_to=imggenerate.all_image_file_path, verbose_name="Фото")
    imagelink = models.TextField(null=True, blank=True, verbose_name="Линк фото товара")
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name="Телефон номер")
    instagram = models.CharField(max_length=200, null=True, blank=True, verbose_name="Инстаграм")
    facebook = models.CharField(max_length=200, null=True, blank=True, verbose_name="Фейсбук")
    whatsapp = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ватсап")
    web = models.CharField(max_length=200, null=True, blank=True, verbose_name="Веб")
    likes = models.IntegerField(default=0, verbose_name="Число лайков")
    views = models.IntegerField(default=0, verbose_name="Число просмотров")
    sale_type = models.CharField(choices=SALE_TYPE, default=RETAIL, max_length=50, verbose_name='Тип продажи')
    isoptovik = models.BooleanField(default=False, verbose_name="Оптовый товар")
    optovikcost = models.FloatField(default=0, verbose_name="Оптовая цена товара")
    priority = models.FloatField(default=0, verbose_name="Приоритет")
    country = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True, verbose_name='Страна')
    city = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True, verbose_name='Город')
    sizes = ArrayField(models.TextField(), null=True, blank=True, verbose_name='Размеры')
    colors = models.ManyToManyField(ModelColor, blank=True, verbose_name='Цвета')
    memory = models.ManyToManyField(ModelMemory, blank=True, verbose_name='Память')
    gender = models.CharField('Пол', blank=True, choices=utils.GENDER, default=utils.MALE, max_length=30)
    gender_type = models.CharField('Пол', blank=True, choices=utils.GENDER, default=utils.MALE, max_length=30)
    images = ArrayField(models.TextField(), null=True, blank=True, verbose_name='Фото')
    descHtml = models.TextField('Описание HTML', blank=True)
    screen = models.ForeignKey(ModelMatrix, models.SET_NULL, null=True, blank=True, verbose_name='Screen ID')


    def __str__(self):
        return self.name


class ModelPackage(models.Model):
    class Meta:
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'

    dateCreated = models.DateTimeField('Дата создания', auto_now_add=True)
    client = models.ForeignKey(Client, models.SET_NULL, null=True, blank=True, verbose_name='Клиент')
    status = models.CharField('Статус', choices=utils.PACKAGE_STATUS, default=utils.CREATED, max_length=100)
    delivery_type = models.CharField('Тип доставки', choices=utils.DELIVERY_TYPE, default=utils.OTHER, max_length=100)
    pid = models.CharField('PID', max_length=100, blank=True)
    senderCountry = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True,
                                      verbose_name='Точка отправки-Страна', related_name='sender_country')
    senderCity = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True,
                                   verbose_name='Точка отправки-Город', related_name='sender_city')
    receiverCountry = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True,
                                      verbose_name='Получатель-Страна', related_name='receiver_country')
    receiverCity = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True, verbose_name='Получатель-Город',
                                     related_name='receiver_city')
    dateArrived = models.DateField('Дата прибытия', blank=True, null=True)
    dateSending = models.DateField('Дата отправки', blank=True, null=True)
    orderNumber = models.CharField('Номер заказа', max_length=100)
    packageData = models.ForeignKey(ModelPackageData, models.SET_NULL, null=True, blank=True, verbose_name='Инф о посылке')
    packageType = models.ForeignKey(ModelPackageType, models.SET_NULL, null=True, blank=True, verbose_name='Тип посылки')
    paymentStatus = models.CharField('Статус оплаты', choices=utils.PAYMENT_STATUS, default=utils.UNPAID, max_length=20)
    clientName = models.CharField('Имя клиента',max_length=200, null=True, blank=True)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты', related_name='clients', blank=True)
    senderName = models.CharField('Имя отправителя', max_length=150, null=True, blank=True)
    senderPhone = models.CharField('Тел отправителя',  max_length=150, null=True, blank=True)
    receiverName = models.CharField('Имя получателя',  max_length=150, null=True, blank=True)
    receiverPhone = models.CharField('Тел получателя',  max_length=150, null=True, blank=True)
    costPerKg = models.FloatField(default=0)
    extraCost = models.FloatField(default=0)
    totalCost = models.FloatField('Общая цена', default=0)
    customExpenses = models.FloatField('Таможенные расходы', default=0)
    comment = models.TextField('Комментарий', default=0)
    tariff = models.ForeignKey(ModelTariff, models.SET_NULL, null=True, blank=True, verbose_name='Тариф')
    length = models.FloatField('Длина', default=0)
    height = models.FloatField('Высота', default=0)
    width = models.FloatField('Ширина', default=0)
    weight = models.FloatField('Вес', default=0)
    image = models.FileField('Изображение',  upload_to=imggenerate.all_image_file_path, null=True, blank=True)
    personal = models.BooleanField('Личная вещь', default=False)
    extraServices = models.ManyToManyField(ModelExtraService, blank=True, verbose_name='Экстра сервис')
    personal_description = models.TextField('Описание личной вещи', null=True, blank=True)
    item = models.ForeignKey(ModelItem, models.SET_NULL, null=True, blank=True, verbose_name='Товар')
    itemCost = models.FloatField('Стоимость за шт', default=0, null=True, blank=True)
    quantity = models.IntegerField('Кол-во', default=1, null=True, blank=True)

    def __str__(self):
        return str(self.orderNumber)


    def save(self, *args, **kwargs):
        if self.pk is not None:
            original = CryptoPay.objects.get(pk=self.pk)
            if original.payment_status != self.payment_status:
                self.create_status_notification()

                if self.payment_status == 'paid':
                    self.is_paid = True

        super().save(*args, **kwargs)

        if self.payment_status == 'paid':
            self.package.paymentStatus = utils.CRYPTO_PAID
            self.package.save()

    def get_status_display(self):
        return dict(utils.PAYMENT_STATUS_CHOICES).get(self.payment_status, self.payment_status)

    def create_status_notification(self):
        if self.client:
            notification = ModelNotification.objects.create(
                client=self.client,
                title="Обновление статуса оплаты",
                text=f"Статус вашей оплаты {self.transaction_hash} был обновлен на {self.get_status_display()}.",
                photo=None
            )
            notification.save()

class ModelAlaket(models.Model):
    class Meta:
        verbose_name = 'Алакет'
        verbose_name_plural = 'Алакет'

    date = models.DateField('Дата', null=True, blank=True)
    dateCreated = models.DateTimeField('Дата создания', auto_now_add=True)
    client = models.ForeignKey(Client, models.CASCADE, verbose_name='Клиент')
    fromCity = models.ForeignKey(ModelCity, models.CASCADE, verbose_name='Из города', related_name='fromCity')
    toCity = models.ForeignKey(ModelCity, models.CASCADE, verbose_name='На город', related_name='toCity')
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание', null=True, blank=True)
    cost = models.FloatField(verbose_name='Расходы', default=0)
    type = models.CharField('Тип', choices=utils.ALAKETEM_TYPE, default=utils.ALAKETEM, max_length=20)
    photo = models.TextField('Фото', blank=True)
    flyTime = models.CharField('Время вылета', max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.title)


class ModelImage(models.Model):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    title = models.CharField('Заголовок', max_length=100)
    image = models.FileField('Фото', upload_to=imggenerate.all_image_file_path)

    def __str__(self):
        return str(self.title)


class ModelAddresses(models.Model):
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    type = models.CharField('Тип', choices=utils.ADDRESS_TYPE, default=utils.DEPOT, max_length=20)
    depot = models.ForeignKey(ModelDepots, models.SET_NULL, null=True, blank=True, verbose_name='Склад')
    country = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True, verbose_name='Страна')
    city = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True, verbose_name='Город')
    address = models.TextField('Адрес', )
    phone = models.CharField('Телефон', max_length=200, blank=True)
    receiverName = models.CharField('Имя получателя', max_length=200, blank=True)
    nameAddress = models.CharField('Название адреса', max_length=255, blank=True)
    user = models.ForeignKey(Client, models.SET_NULL, null=True, blank=True, verbose_name='Клиент')

    def __str__(self):
        return str(self.address)


class ModelRequests(models.Model):
    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    package = models.OneToOneField(ModelPackage, on_delete=models.CASCADE, related_name='request', null=True, blank=True)
    senderName = models.CharField('Имя отправителя', max_length=100, blank=True)
    senderPhone = models.CharField('Телефон номер отправителя', max_length=100, blank=True)
    receiverName = models.CharField('Имя получателя', max_length=100, blank=True)
    receiverPhone = models.CharField('Имя номер получателя', max_length=100, blank=True)
    serviceName = models.CharField('Наименование услуги', max_length=100, blank=True)
    fromCountry = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True, related_name='from_countryw')
    fromCity = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True, related_name='from_cityw')
    toCountry = models.ForeignKey(ModelCountry, models.SET_NULL, null=True, blank=True, related_name='to_countryw')
    toCity = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True, related_name='to_cityw')
    packageType = models.ForeignKey(ModelPackageType, models.SET_NULL, null=True, blank=True, verbose_name='Тип посылки')
    packageData = models.ForeignKey(ModelPackageData, models.SET_NULL, null=True, blank=True, verbose_name='О посылке')
    dateSending = models.DateField('Дата отправки', blank=True)
    dateCreated = models.DateTimeField('Дата оформления', auto_now_add=True)
    phone = models.CharField('Телефон', max_length=50)
    telegram = models.TextField('Телеграм', blank=True)
    comment = models.TextField('Комментарий', blank=True)
    client = models.ForeignKey(Client, models.SET_NULL, null=True, blank=True, verbose_name='Клиент')
    weight = models.FloatField('Масса', default=0)
    length = models.FloatField('Длина', default=0)
    height = models.FloatField('Высота', default=0)
    width = models.FloatField('Ширина', default=0)
    cost = models.FloatField('Расходы', default=0)
    archive = models.BooleanField('Архив', default=False)
    trackNumbers = models.CharField('Номер дорожки', blank=True, max_length=255)
    extraServices = models.ManyToManyField(ModelExtraService, verbose_name='Экстра сервисы', blank=True)
    premium = models.BooleanField('Премиум', default=False)
    address = models.ForeignKey(ModelAddresses, models.SET_NULL, null=True, blank=True, verbose_name='Адрес')
    is_private = models.BooleanField('Приватный', default=False)
    private_item_description = models.TextField('Описание приватного товара', blank=True, null=True)
    product_link = models.TextField('Ссылка на товар', blank=True, null=True)

    def __str__(self):
        return str(self.id)


class DepotUser(User):
    class Meta:
        verbose_name = 'Пользователь депо'
        verbose_name_plural = 'Пользователи депо'

    depot = models.ForeignKey(ModelDepots, models.SET_NULL, null=True, blank=True, verbose_name='Депо')

    def __str__(self):
        return str(self.login)

    def clean(self):
        self.user_type = DEPOT_USER


class BuyerBanners(models.Model):
    class Meta:
        verbose_name = 'Баннер для покупателя'
        verbose_name_plural = 'Баннеры для покупателей'

    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст', blank=True)
    photo = models.ImageField('Фото', upload_to='uploads/', null=True, blank=True)
    order = models.FloatField('Order', default=0)

    def __str__(self):
        return str(self.title)


class CartRequest(models.Model):
    class Meta:
        verbose_name = 'Карзина запросов'
        verbose_name_plural = 'Карзины запросов'

    link = models.TextField('Ссылка', blank=True)
    comment = models.TextField('Комментарий', blank=True)
    itemCost = models.FloatField('Стоимость за шт', default=0, null=True, blank=True)
    quantity = models.IntegerField('Кол-во', default=1, null=True, blank=True)

    def __str__(self):
        return str(self.comment)


class ModelBuyerRequest(models.Model):
    class Meta:
        verbose_name = 'Заявка покупателя'
        verbose_name_plural = 'Заявки покупателей'

    CREATED = 'created'
    CONFIRMED = 'confirmed'
    IN_PROGRESS = 'in_progress'
    BOUGHT = 'bought'
    SENT = 'sent'
    AWAITING_PAYMENT = 'Ожидает оплат'
    PAID = 'Оплачена'
    IN_WORK = 'Взята в работу'
    PURCHASED = 'Товар выкуплен'
    BUYER_REQUEST_STATUS = (
        (CREATED, 'Создано'),
        (CONFIRMED, 'Подтверждено'),
        (IN_PROGRESS, 'В процессе'),
        (BOUGHT, 'Куплено'),
        (SENT, 'Отправлено'),
        (AWAITING_PAYMENT, 'Ожидает оплаты'),
        (PAID, 'Оплачена'),
        (IN_WORK, 'Взята в работу'),
        (PURCHASED, 'Товар выкуплен')
    )

    link = models.TextField('Ссылка', blank=True)
    phone = models.CharField('Телефон номер', max_length=200)
    name = models.CharField('Название', max_length=200)
    client = models.ForeignKey(Client, models.SET_NULL, null=True, blank=True, verbose_name='Клиент')
    dateCreated = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.CharField('Статус', choices=BUYER_REQUEST_STATUS, default=utils.CREATED, max_length=50)
    comment = models.TextField('Комментарий', blank=True)
    cart_request = models.ManyToManyField(CartRequest, blank=True, verbose_name='Корзина запросов')
    active = models.BooleanField('Статус активности', default=True)
    paid = models.BooleanField('Оплачено', default=False)
    totalCost = models.FloatField('Стоимость', default=0)
    info = models.TextField('Информация', blank=True)
    trackNumbers = models.CharField('Номер дорожки', blank=True, max_length=255)

    def __str__(self):
        return str(self.name)


class ModelColorSize(models.Model):
    item = models.ForeignKey(ModelItem, on_delete=models.CASCADE, related_name='color_sizes')
    color = models.ForeignKey(ModelColor, on_delete=models.CASCADE,verbose_name='Hазмер цвета', related_name='color_sizes')
    size = models.CharField(max_length=50, verbose_name='Размер')

    class Meta:
        verbose_name = 'Цвет и Размер'
        verbose_name_plural = 'Цвета и Размеры'

    def __str__(self):
        return f"{self.color.nameRu} - {self.size}"


class CartItems(models.Model):
    """Models for images"""
    item = models.ForeignKey(ModelItem, on_delete=models.SET_NULL, null=True, blank=True,  verbose_name="Товар")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    color = models.ForeignKey(ModelColor, models.SET_NULL, null=True, verbose_name='Цвет')
    size = models.TextField(verbose_name="Размер", null=True, blank=True)
    memory = models.ForeignKey(ModelMemory, models.SET_NULL, null=True, blank=True, verbose_name='Память')

    class Meta:
        verbose_name = ("Товар")
        verbose_name_plural = ("Товары")


class ModelOrder(models.Model):
    class Meta:
        verbose_name = ("Заказ")
        verbose_name_plural = ("Заказы")

    store = models.IntegerField(default=0, verbose_name="ID Магазина")
    totalCost = models.FloatField(default=0, verbose_name="Общая сумма")
    user = models.CharField(max_length=200, null=True, blank=True, verbose_name="Пользователь")
    addresses = models.ForeignKey(ModelAddresses, models.SET_NULL, null=True, blank=True, verbose_name='Адреса')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name="Телефон номер")
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True, verbose_name="Комментарии")
    storeName = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название магазина")
    storeLogo = models.CharField(max_length=200, null=True, blank=True, verbose_name="Лого магазина")
    status = models.CharField(choices=utils.ORDER_STATUS, default=utils.NEW, verbose_name="Статус", max_length=50)
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Дата")
    isoptovik = models.BooleanField(default=False, verbose_name="Оптовик?")
    bonus = models.FloatField(verbose_name='Бонус', default=0)
    pay_status = models.BooleanField(verbose_name='Статус оплаты', default=False)
    client = models.ForeignKey(to=Client, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='ID пользователя')
    items = models.ManyToManyField(CartItems, verbose_name='Карзина', blank=True)

    def __str__(self):
        return str(self.id)


class ModelVideo(models.Model):
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    title = models.CharField('Заголовок', max_length=100)
    video = models.FileField('Видео', upload_to='video/')

    def __str__(self):
        return str(self.title)


class WantedItems(models.Model):
    class Meta:
        verbose_name = 'Нужный товар'
        verbose_name_plural = 'Нужные товары'

    description = models.TextField('Описание', blank=True)
    photo = models.TextField('Фото', blank=True)

    def __str__(self):
        return str(self.description)


class ModelItemSearchRequest(models.Model):
    class Meta:
        verbose_name = 'Запрос на поиск товара'
        verbose_name_plural = 'Запросы на поиск товара'

    client = models.ForeignKey(Client, models.SET_NULL, null=True, blank=True, verbose_name='Клиент')
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон номер', max_length=100)
    wantedItems = models.ManyToManyField(WantedItems, blank=True, verbose_name='Товары поиска')
    description = models.TextField('Описание', blank=True)
    # photo = models.TextField('Фото', blank=True)
    active = models.BooleanField('Статус активности', default=True)

    def __str__(self):
        return str(self.name)

class CryptoPay(models.Model):
    client = models.ForeignKey(Client, models.CASCADE, related_name='crypto_pay')
    wallet = models.ForeignKey(ModelWallet, models.PROTECT, related_name='crypto_pay', null=True)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES, verbose_name='Тип оплаты')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default=UNPAID, verbose_name='Статус оплаты')
    transaction_hash = models.CharField(max_length=255, verbose_name='Хеш транзакции')
    amount = models.FloatField('Сумма оплаты', default=0)  # Add the amount field here
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    send_receipt = models.BooleanField(default=False, verbose_name='Отправлять квитанцию?')
    receipt_email = models.EmailField(max_length=254, verbose_name='Email для квитанции', blank=True, null=True)
    is_paid = models.BooleanField('Оплачено', default=False)

    class Meta:
        verbose_name = 'Оплата криптой'
        verbose_name_plural = 'Оплаты криптой'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.transaction_hash} - {self.client}'

    def save(self, *args, **kwargs):
        is_status_changed = False
        if self.pk is not None:
            original = CryptoPay.objects.get(pk=self.pk)
            if original.payment_status != self.payment_status:
                is_status_changed = True

        super().save(*args, **kwargs)

        if is_status_changed and self.payment_status == 'paid':  # Ensure 'paid' matches your actual choice
            self.update_wallet_amount()

    def get_status_display(self):
        return dict(PAYMENT_STATUS_CHOICES).get(self.payment_status, self.payment_status)

    def create_status_notification(self):
        if self.client:
            notification = ModelNotification.objects.create(
                client=self.client,
                title="Обновление статуса оплаты",
                text=f"Статус вашей оплаты {self.transaction_hash} был обновлен на {self.get_status_display()}.",
                photo=None
            )
            notification.save()

    def update_wallet_amount(self):
        if self.wallet:
            self.wallet.amount += self.amount
            self.wallet.save()
