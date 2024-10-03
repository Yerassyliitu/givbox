from django.db import models

from category import imggenerate


class ModelWH(models.Model):
    class Meta:
        verbose_name = 'Робачие часы'
        verbose_name_plural = 'Робачие часы'

    mondayStart = models.CharField(max_length=10, blank=True, verbose_name='Начало понедельник')
    mondayEnd = models.CharField(max_length=10, blank=True, verbose_name='Конец понедельник')
    tuesdayStart = models.CharField(max_length=10, null=True, blank=True, verbose_name='Вторник: начало')
    tuesdayEnd = models.CharField(max_length=10, null=True, blank=True, verbose_name='Вторник: конец')
    wednesdayStart = models.CharField(max_length=10, null=True, blank=True, verbose_name='Среда: начало')
    wednesdayEnd = models.CharField(max_length=10, null=True, blank=True, verbose_name='Среда: конец')
    thursdayStart = models.CharField(max_length=10, null=True, blank=True, verbose_name='Четверг: начало')
    thursdayEnd = models.CharField(max_length=10, null=True, blank=True, verbose_name='Четверг: конец')
    fridayStart = models.CharField(max_length=10, null=True, blank=True, verbose_name='Пятница: начало')
    fridayEnd = models.CharField(max_length=10, null=True, blank=True, verbose_name='Пятница: конец')
    satStart = models.CharField(max_length=10, null=True, blank=True, verbose_name='Суббота: начало')
    satEnd = models.CharField(max_length=10, null=True, blank=True, verbose_name='Суббота: конец')
    sundayStart = models.CharField(max_length=10, null=True, blank=True, verbose_name='Воскресенье: начало')
    sundayEnd = models.CharField( max_length=10, null=True, blank=True, verbose_name='Воскресенье: конец')

    def __str__(self):
        return str(self.mondayStart)


class ModelContact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    phone = models.CharField('Номер телефона', max_length=50)
    email = models.EmailField(verbose_name='Электронная почта', max_length=256)
    messangers = models.TextField('Ссылка', blank=True)

    def __str__(self):
        return str(self.phone)


class ModelCountry(models.Model):
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    nameKg = models.CharField('Мамлекет', max_length=100)
    nameEn = models.CharField('Country', max_length=100)
    nameRu = models.CharField('Страна', max_length=100)
    icon = models.ImageField('Флаг', upload_to=imggenerate.all_image_file_path, null=True, blank=True)
    code = models.TextField('Код', blank=True)
    phoneCode = models.CharField('Код телефона', max_length=100, blank=True)

    def __str__(self):
        return str(self.nameRu)


class ModelCity(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    nameKg = models.CharField('Шаар', max_length=100)
    nameEn = models.CharField('City', max_length=100)
    nameRu = models.CharField('Город', max_length=100)
    country = models.ForeignKey(ModelCountry, models.CASCADE, verbose_name='Страна')
    code = models.TextField('Код', blank=True)

    def __str__(self):
        return str(self.nameRu)


class ModelPackageType(models.Model):
    class Meta:
        verbose_name = 'Тип посылки'
        verbose_name_plural = 'Типы посылок'

    nameKg = models.CharField('Пакеттин аталышы', max_length=100)
    nameEn = models.CharField('Package name', max_length=100)
    nameRu = models.CharField('Название пакета', max_length=100)
    icon = models.ImageField('Изображение', upload_to=imggenerate.all_image_file_path, null=True, blank=True)

    def __str__(self):
        return str(self.nameRu)


class ModelNotification(models.Model):
    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    client = models.ForeignKey('user.Client', on_delete=models.CASCADE, null=True, related_name='notifications')
    title = models.CharField('Заголовок', max_length=200)
    date = models.DateTimeField('Дата и время', auto_now_add=True)
    text = models.TextField('Текст')
    photo = models.TextField('Ссылка на фото', null=True, blank=True)
    read = models.BooleanField('Статус чтения', default=False)

    def __str__(self):
        return str(self.title)


class ModelCosts(models.Model):
    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

    fromCity = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True, verbose_name='Из города',
                                 related_name='from_city')
    toCity = models.ForeignKey(ModelCity, models.SET_NULL, null=True, blank=True, verbose_name='В город',
                               related_name='to_city')
    costPerKg = models.FloatField('Стоимость за kg', default=0)
    costPerKgMy = models.FloatField('Стоимость за kg my', default=0)
    costPerVW = models.FloatField('Стоимость за VW', default=0)


class ModelTariff(models.Model):
    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    nameKg = models.CharField('Кыргызча аталышы', max_length=100)
    nameEn = models.CharField('Tariff name', max_length=100)
    nameRu = models.CharField('Название', max_length=100)
    icon = models.TextField('Иконка', blank=True)
    extraCost = models.FloatField('Дополнительная стоимость', default=0)

    def __str__(self):
        return str(self.nameKg)


class ModelCurrency(models.Model):
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    currency = models.CharField('Валюта', max_length=100)
    oneGBIn = models.FloatField('One G BIn', default=0)
    icon = models.ImageField('Иконка', upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return str(self.currency)


class ModelWebsite(models.Model):
    class Meta:
        verbose_name = 'Веб сайт'
        verbose_name_plural = 'Веб сайты'

    name = models.CharField('Название', max_length=200)
    icon = models.ImageField('Иконка', upload_to='uploads/')
    link = models.TextField('Ссылка', blank=True)

    def __str__(self):
        return str(self.name)


class StoreCategory(models.Model):
    """Model for store categories(types of stores(electronics, etc))"""
    nameEn = models.CharField(max_length=200, null=True, verbose_name="Название на английском")
    nameRus = models.CharField(max_length=200, null=True, verbose_name="Название на русском")
    nameKg = models.CharField(max_length=200, null=True, verbose_name="Название на кыргызком")
    icon = models.ImageField(null=True, upload_to=imggenerate.all_image_file_path, verbose_name="Фото")
    priority = models.PositiveIntegerField(verbose_name='Приоритет', default=0)

    def __str__(self):
        return self.nameRus

    class Meta:
        ordering = ('id',)
        verbose_name = ("Категория магазина")
        verbose_name_plural = ("Категории магазинов")


class Category(models.Model):
    """Category model"""
    nameEn = models.CharField(max_length=200, null=True, verbose_name="Название на английском")
    nameRus = models.CharField(max_length=200, null=True, verbose_name="Название на русском")
    nameKg = models.CharField(max_length=200, null=True, verbose_name="Название на кыргызком")
    isoptovik = models.BooleanField(default=False, verbose_name="Оптовик?")
    priority = models.FloatField(default=0, verbose_name="Приоритет")

    icon = models.ImageField(upload_to=imggenerate.all_image_file_path, verbose_name="Фото", null=True, blank=True)
    store = models.ManyToManyField('user.Store', blank=True, verbose_name="Магазин")

    def __str__(self):
        return self.nameRus

    class Meta:
        ordering = ('id',)
        verbose_name = ("Категория")
        verbose_name_plural = ("Категории")


class SubCategory(models.Model):
    """SubCategory model"""
    nameEn = models.CharField(max_length=200, null=True, verbose_name="Название на английском")
    nameRus = models.CharField(max_length=200, null=True, verbose_name="Название на русском")
    nameKg = models.CharField(max_length=200, null=True, verbose_name="Название на кыргызком")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")

    def __str__(self):
        return self.nameRus

    class Meta:
        ordering = ('id',)
        verbose_name = ("Субкатегория")
        verbose_name_plural = ("Субгатегории")


class ModelFranchiseRequest(models.Model):
    class Meta:
        verbose_name = 'Франшиза'
        verbose_name_plural = 'Франшизы'

    name = models.CharField('Название', max_length=200)
    email = models.EmailField('Электронная почта', unique=True)
    phone = models.CharField('Телефон номер', max_length=200, blank=True)
    archive = models.BooleanField('Архив', default=False)

    def __str__(self):
        return str(self.name)


class ModelGbBusinessRequest(models.Model):
    class Meta:
        verbose_name = 'Бизнес-запрос модель Gb'
        verbose_name_plural = 'Бизнес-запрос модели Gb'

    name = models.CharField('Название', max_length=200)
    email = models.EmailField('Электронная почта', unique=True)
    phone = models.CharField('Телефон номер', max_length=200, blank=True)
    info = models.TextField('Информация', blank=True)
    file = models.TextField('Файл', blank=True)
    archive = models.BooleanField('Архив', default=False)

    def __str__(self):
        return str(self.name)


class ModelFile(models.Model):
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    title = models.CharField('Заголовок', max_length=200)
    file = models.FileField('Файл', upload_to='files/')
    request = models.ForeignKey('core.ModelRequests', on_delete=models.CASCADE, related_name='file', null=True, blank=True)

    def __str__(self):
        return str(self.title)


class ModelExtraService(models.Model):
    class Meta:
        verbose_name = 'Экстра сервис'
        verbose_name_plural = 'Экстра сервисы'

    nameRu = models.CharField('Название', max_length=100)
    nameEn = models.CharField('Name', max_length=100, blank=True)
    nameKg = models.CharField('Аталышы', max_length=100, blank=True)
    icon = models.TextField('Иконка', blank=True)
    infoRu = models.TextField('Информация', blank=True)
    infoEn = models.TextField('Information', blank=True)
    infoKg = models.TextField('Маалымат', blank=True)
    cost = models.FloatField('Стоимость', default=0)

    def __str__(self):
        return str(self.nameRu)


class ModelColor(models.Model):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    color = models.CharField('Цвет', max_length=200)
    image = models.TextField('Рисунок', blank=True)
    nameRu = models.CharField('Название', max_length=100)
    nameKg = models.CharField('Аталышы', max_length=100, blank=True)
    nameEn = models.CharField('Name', max_length=100, blank=True)

    def __str__(self):
        return str(self.nameRu)


class ModelMemory(models.Model):
    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектация'

    ram = models.TextField('ОЗУ', max_length=100, null=True)
    storage = models.TextField('Объем памяти', max_length=100, null=True)
    addCost = models.FloatField('Add cost', default=0, null=True)

    def __str__(self):
        return str(self.ram)


class ModelCore(models.Model):
    class Meta:
        verbose_name = 'Ядро'
        verbose_name_plural = 'Ядра'

    equipment = models.OneToOneField(ModelMemory, on_delete=models.CASCADE, related_name='cores')
    cpu = models.CharField('CPU', max_length=100)
    gpu = models.CharField('GPU', max_length=100)

    def __str__(self):
        return f'CPU: {self.cpu}, GPU: {self.gpu}'


class ModelMatrix(models.Model):
    class Meta:
        verbose_name = 'Монитор'
        verbose_name_plural = 'Монитор'

    diagonal = models.FloatField('Диагональ', default=0, null=True)
    matrix_type = models.TextField('Тип матрицы', max_length=100, null=True)
    resolution = models.TextField('Разрешение', max_length=100, null=True)
    frame_frequency = models.TextField('Частота кадров', max_length=100, null=True)
    screen = models.FloatField('Screen', default=0, null=True)

    def __str__(self):
        return str(self.matrix_type)
    
class ModelCurrencyFromUsd(models.Model):
    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курс валют'

    som = models.FloatField('Сом', default=0)
    rub = models.FloatField('Рубль', default=0)
    euro = models.FloatField('Евро', default=0)
    tenge = models.FloatField('Тенге', default=0)
    sum = models.FloatField('Сум', default=0)
    yuan = models.FloatField('Юань', default=0)

    def __str__(self):
        return str(self.rub)
