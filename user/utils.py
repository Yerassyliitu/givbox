DOLLAR = 'dollar'
RUBLE = 'ruble'
SOM = 'som'

WALLET_CURRENCY = ((SOM, 'сом'), (RUBLE, 'рубль'), (DOLLAR, 'доллар'))


CLIENT = 'client'
ADMIN = 'admin'
BUYER = 'buyer'
DEPOT_USER = 'depot_user'
SUPPORT_USER = 'support_user'
STORE = 'store'
SHOP_USER = 'shop_user'
USER_TYPE = ((CLIENT, 'Клиент'), (ADMIN, 'Админ'), (BUYER, 'Покупатель'), (DEPOT_USER, 'Склад'),
             (SUPPORT_USER, 'Поддержка'), (STORE, 'Магазин'), (SHOP_USER, 'Клиент магазина'))


RETAIL = 'retail'
WHOLESALE = 'wholesale'
BOTH = 'both'
SALE_TYPE = ((RETAIL, 'розница'), (WHOLESALE, 'Оптом'), (BOTH, 'Оптом и розница'))
