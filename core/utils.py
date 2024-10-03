CREATED = 'CREATED'
ON_WAY = 'on_way'
ARRIVED = 'arrived'
DONE = 'done'

PACKAGE_STATUS = (
    ('CREATED', 'Создан'),
    ('RECEIVED_AT_WAREHOUSE', 'Получен на складе'),
    ('SENT', 'Отправлен'),
    ('ON_WAY', 'В пути'),
    ('ARRIVED_TRANSIT_COUNTRY', 'Прибыл в транзитную страну'),
    ('SENT_TO_DESTINATION_COUNTRY', 'Отправлен в страну назначения'),
    ('ON_WAY_TO_DESTINATION', 'В пути'),
    ('ARRIVED_DESTINATION_COUNTRY', 'Прибыл в страну назначения'),
    ('CUSTOMS_CLEARANCE', 'Проходит таможенное оформление'),
    ('RECEIVED_AT_DESTINATION_WAREHOUSE', 'Получен на складе страны назначения'),
    ('CDEK', 'Посылка пришла в СДЭК'),
    ('DELIVERED_TO_RECIPIENT', 'Отправлен адресату'),
)

OTHER = 'Другая транспортная доставка'
DELIVERY_TYPE = (
    ('CDEK', 'СДЭК'),
    ('YANDEX', 'Яндекс доставка'),
    ('OTHER', 'Другая транспортная доставка'),
)
PAID = 'paid'
UNPAID = 'unpaid'
CRYPTO_PAID = 'Оплачено криптой'
PAYMENT_STATUS = ((PAID, 'Оплачено'), (UNPAID, 'Не оплачено'), (CRYPTO_PAID, 'Оплачено криптой'))

ALAKETEM = 'alaketem'
BEREM = 'berem'
ALAKETEM_TYPE = ((ALAKETEM, 'Возьму собой'), (BEREM, 'Отдам'))

IN = 'in'
OUT = 'out'
BOTH = 'both'
DEPOT_TYPE = ((IN, 'in'), (OUT, 'out'), (BOTH, 'both'))

DEPOT = 'depot'
CUSTOM = 'custom'
ADDRESS_TYPE = ((DEPOT, 'Склад'), (CUSTOM, 'Custom'))

NEW = 'new'
PACKING = 'packing'
DELIVERING = 'delivering'
DELIVERED = 'delivered'
REJECTED = 'rejected'
CLIENT_REJECT = 'client_reject'
ORDER_STATUS = ((NEW, 'Новый'), (PACKING, 'Упаковывается'), (DELIVERING, 'В пути'), (DELIVERED, 'Доставлено'),
                (REJECTED, 'Отказано'), (CLIENT_REJECT, 'Отменен'))

MALE = 'male'
FEMALE = 'female'
KIDS = 'kids'
ANY = 'any'
GENDER = ((MALE, 'Мужской'), (FEMALE, 'Женский'), (KIDS, 'Детский'), (ANY, 'Для всех'))

PAYMENT_TYPE_CHOICES = [
    ('parcel', 'Оплата за посылку'),
    ('wallet', 'Пополнение кошелька'),
    ('store', 'Оплата за товар в магазине'),
    ('item', 'Заявка на покупку товара')
]

PAYMENT_STATUS_CHOICES = [
    ('paid', 'Оплачено'),
    ('waiting', 'Ожидается подтверждение оплаты криптой'),
    ('unpaid', 'Не оплачено'),
]
