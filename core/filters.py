from django_filters import FilterSet
from django_filters import rest_framework as filters
from core import models
from user.models import Store


class DepotFilter(FilterSet):
    country = filters.CharFilter('country')
    city = filters.CharFilter('city')
    maxAmount = filters.RangeFilter('maxAmount', lookup_expr='lte')
    types = filters.CharFilter('types')
    active = filters.BooleanFilter('active')

    class Meta:
        models = models.ModelDepots
        fields = ('country', 'city', 'maxAmount', 'types', 'active')


class CharFilterOR(filters.BaseInFilter, filters.CharFilter):
    pass


class PackageFilter(FilterSet):
    client = filters.CharFilter('client')
    senderCountry = filters.CharFilter('senderCountry')
    senderCity = filters.CharFilter('senderCity')
    receiverCountry = filters.CharFilter('receiverCountry')
    receiverCity = filters.CharFilter('receiverCity')
    packageType = filters.CharFilter('packageType')
    paymentStatus = filters.CharFilter('paymentStatus')
    status = filters.CharFilter('status')
    clients = CharFilterOR(field_name='clients', lookup_expr='in')
    # clients = filters.ModelMultipleChoiceFilter(field_name='clients', to_field_name='clients',
    #                                             queryset=models.ModelPackage.objects.all())
    orderNumber = filters.CharFilter('orderNumber')
    tariff = filters.CharFilter('tariff')

    class Meta:
        models = models.ModelPackage
        fields = ('client', 'senderCountry', 'senderCity', 'receiverCountry', 'receiverCity', 'packageType',
                  'paymentStatus', 'status', 'clientName', 'clients', 'tariff')


class AlaketFilter(FilterSet):
    startDate = filters.DateFilter('date', lookup_expr='gte')
    endDate = filters.DateFilter('date', lookup_expr='lte')
    toCity = filters.CharFilter('toCity')
    fromCity = filters.CharFilter('fromCity')

    class Meta:
        models = models.ModelAlaket
        fields = ('startDate', 'endDate', 'toCity', 'fromCity')


class RequestFilter(FilterSet):
    fromCountry = filters.CharFilter('fromCountry')
    fromCity = filters.CharFilter('fromCity')
    toCountry = filters.CharFilter('toCountry')
    toCity = filters.CharFilter('toCity')
    client = filters.CharFilter('client')
    archive = filters.BooleanFilter('archive')
    premium = filters.BooleanFilter('premium')

    class Meta:
        models = models.ModelRequests
        fields = ('fromCountry', 'fromCity', 'toCountry', 'toCity', 'client', 'archive', 'premium')


class AddressesFilter(FilterSet):
    user = filters.CharFilter('user')

    class Meta:
        models = models.ModelAddresses
        fields = ('user', )


class BuyerRequestFilter(FilterSet):
    status = filters.CharFilter('status')
    client = filters.CharFilter('client')
    active = filters.BooleanFilter('active')

    class Meta:
        models = models.ModelBuyerRequest
        fields = ('status', 'client', 'active')


class ItemFilter(FilterSet):
    category = filters.CharFilter('category')
    subcategory = filters.CharFilter('subcategory')
    country = filters.CharFilter('country')
    city = filters.CharFilter('city')

    uniqueid = filters.CharFilter('uniqueid')
    issale = filters.CharFilter('issale')
    isoptovik = filters.CharFilter('isoptovik')

    supplier__visibility = filters.BooleanFilter('supplier__visibility')

    min_cost = filters.CharFilter(field_name="cost", lookup_expr='gte')
    max_cost = filters.CharFilter(field_name="cost", lookup_expr='lte')
    gender_type = filters.CharFilter("gender_type")
    supplier = CharFilterOR(field_name='supplier', lookup_expr='in')
    sizes = filters.CharFilter(method='filter_by_sizes')
    # suppliers = filters.ModelMultipleChoiceFilter(queryset=Store.objects.all())

    class Meta:
        models = models.ModelItem
        fields = ('uniqueid', 'category', 'subcategory', 'min_cost', 'max_cost', 'min_cost',
                  'isoptovik', 'issale', 'supplier', 'country', 'city', 'gender_type', 'sizes')

    def filter_by_sizes(self, queryset, name, value):
        sizes_list = value.split(';')
        for size in sizes_list:
            queryset = queryset.filter(sizes__contains=[size.strip()])
        return queryset


class OrderFilter(FilterSet):
    store = filters.CharFilter('store')
    isoptovik = filters.CharFilter('isoptovik')
    start_date = filters.DateFilter(field_name="date", lookup_expr='gte')
    end_date = filters.DateFilter(field_name="date", lookup_expr='lte')
    client = filters.CharFilter('client')
    status = filters.CharFilter('status')
    pay_status = filters.BooleanFilter('pay_status')

    class Meta:
        models = models.ModelOrder
        fields = ('store', 'start_date', 'end_date', 'isoptovik', 'client', 'status', 'pay_status')


class ItemSearchFilter(FilterSet):
    client = filters.CharFilter('client')
    active = filters.BooleanFilter('active')

    class Meta:
        models = models.ModelItemSearchRequest
        fields = ('client', 'active')


class CryptoPaymentFilter(FilterSet):
    payment_type = filters.CharFilter('payment_type')

    class Meta:
        models = models.CryptoPay
        fields = ('payment_type', )