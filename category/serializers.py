from rest_framework import serializers

from category import models
from user.models import Client


class HourWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelWH
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelContact
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCountry
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'icon', 'code', 'phoneCode')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCity
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'country', 'code')


class CitySerializerGet(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = models.ModelCity
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'country', 'code')


class PackageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelPackageType
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'icon')


class ClientNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'fullname')


class NotificationSerializer(serializers.ModelSerializer):
    client = ClientNotificationSerializer(read_only=True)
    class Meta:
        model = models.ModelNotification
        fields = ('client', 'id', 'date', 'title', 'text', 'read')


class NotificationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelNotification
        fields = ('title', 'date', 'text', 'photo', 'read')


class CostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCosts
        fields = ('id', 'fromCity', 'toCity', 'costPerKg', 'costPerKgMy', 'costPerVW')


class CostsSerializerGet(serializers.ModelSerializer):
    fromCity = CitySerializerGet()
    toCity = CitySerializerGet()

    class Meta:
        model = models.ModelCosts
        fields = ('id', 'fromCity', 'toCity', 'costPerKg', 'costPerKgMy', 'costPerVW')


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelTariff
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'icon', 'extraCost')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCurrency
        fields = ('id', 'currency', 'oneGBIn', 'icon')


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelWebsite
        fields = ('id', 'name', 'icon', 'link')


class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StoreCategory
        fields = ('id', 'nameEn', 'nameRus', 'nameKg', 'icon', 'priority')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'nameEn', 'nameRus', 'nameKg', 'icon', 'priority', 'isoptovik', 'store')


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = ('id', 'nameEn', 'nameRus', 'nameKg', 'category')


class FranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelFranchiseRequest
        fields = ('id', 'name', 'email', 'phone', 'archive')


class BusinessRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelGbBusinessRequest
        fields = ('id', 'name', 'email', 'phone', 'info', 'file', 'archive')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelFile
        fields = ('id', 'title', 'file')


class ExtraServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelExtraService
        fields = ('id', 'nameRu', 'nameEn', 'nameKg', 'icon', 'infoRu', 'infoEn', 'infoKg', 'cost')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelColor
        fields = ('id', 'nameRu', 'nameEn', 'nameKg', 'color', 'image')


class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCore
        fields = ('cpu', 'gpu',)


class MemorySerializer(serializers.ModelSerializer):
    cores = CoreSerializer(required=False)
    class Meta:
        model = models.ModelMemory
        fields = ('id', 'ram', 'storage', 'cores', 'addCost')

    def create(self, validated_data):
        core_data = validated_data.pop('cores', None)
        memory = models.ModelMemory.objects.create(**validated_data)

        if core_data:
            models.ModelCore.objects.create(equipment=memory, **core_data)

        return memory

    def update(self, instance, validated_data):
        core_data = validated_data.pop('cores', None)

        instance.ram = validated_data.get('ram', instance.ram)
        instance.storage = validated_data.get('storage', instance.storage)
        instance.addCost = validated_data.get('addCost', instance.addCost)
        instance.save()

        if core_data:
            if hasattr(instance, 'cores'):
                instance.core.delete()
            models.ModelCore.objects.create(equipment=instance, **core_data)

        return instance


class MatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelMatrix
        fields = ('id', 'diagonal', 'matrix_type', 'resolution', 'frame_frequency', 'screen')

class CurrencyFromUsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCurrencyFromUsd
        fields = ('id', 'som', 'rub', 'tenge', 'euro', 'sum', 'yuan')
