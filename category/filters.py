from django_filters import FilterSet
from django_filters import rest_framework as filters
from category import models


class CityFilter(FilterSet):
    country = filters.CharFilter('country')

    class Meta:
        models = models.ModelCity
        fields = ('country', )


class CategoryFilter(FilterSet):
    store = filters.CharFilter('store')
    priority = filters.CharFilter('priority')

    class Meta:
        models = models.Category
        fields = ('store', 'priority')


class SubCategoryFilter(FilterSet):
    category = filters.CharFilter('category')

    class Meta:
        models = models.SubCategory
        fields = ('category', )


class NotificationFilter(FilterSet):
    class Meta:
        models = models.ModelNotification
        fields = ('date', )