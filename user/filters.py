from django_filters import FilterSet
from django_filters import rest_framework as filters

from user import models


class ClientFilters(FilterSet):
    city = filters.CharFilter('city')
    country = filters.CharFilter('country')

    class Meta:
        model = models.Client
        fields = ('city', 'country', )


class EmployeeFilter(FilterSet):
    active = filters.BooleanFilter('active')

    class Meta:
        model = models.Employee
        fields = ('active', )


class BuyerFilter(FilterSet):
    countries = filters.ModelMultipleChoiceFilter(queryset=models.ModelCountry.objects.all())
    websites = filters.ModelMultipleChoiceFilter(queryset=models.ModelWebsite.objects.all())

    class Meta:
        model = models.BuyerUser
        fields = ('countries', 'websites')


class StoreFilter(FilterSet):
    storeCategory = filters.CharFilter('storeCategory')
    visibility = filters.CharFilter('visibility')

    class Meta:
        models = models.Store
        fields = ('storeCategory', 'visibility')


class WalletHistoryFilter(FilterSet):
    client = filters.CharFilter('client')

    class Meta:
        models = models.ModelWalletHistory
        fields = ('client', )
