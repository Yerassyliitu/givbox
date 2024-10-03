from django.http import QueryDict
from rest_framework import serializers
import json
from category.models import ModelColor, ModelFile
from category.serializers import CountrySerializer, CitySerializer, ContactsSerializer, HourWorkSerializer, \
    PackageTypeSerializer, CategorySerializer, ExtraServiceSerializer, SubCategorySerializer, ColorSerializer, \
    MemorySerializer, MatrixSerializer, FileSerializer
from core import models
from core.models import ModelColorSize, ModelItem, ModelRequests, ModelPackage
from user import utils
from user.serializers import ClientSerializer, StoreSerializerOpen


class DepotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelDepots
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'address', 'maxAmount', 'country', 'extraServices', 'isCommercial',
                  'city', 'contacts', 'workingHours', 'images', 'lat', 'lon', 'types', 'infoEn', 'infoRu', 'infoKg',
                  'active', 'video', 'cityStr', 'instructionsRu', 'instructionsKg', 'instructionsEn', 'link_zip',
                  'nameStr', 'nameStart', 'stateStr', 'surnameStr', 'email')


class PackageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelPackageData
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'infoRu', 'infoKg', 'infoEn', 'length', 'height', 'width',
                  'weight', 'order', 'icon')


class DepotSerializerGet(serializers.ModelSerializer):
    country = CountrySerializer()
    city = CitySerializer()
    contacts = ContactsSerializer()
    workingHours = HourWorkSerializer(many=True, required=False, allow_null=True)
    extraServices = ExtraServiceSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = models.ModelDepots
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'address', 'maxAmount', 'country', 'extraServices', 'isCommercial',
                  'city', 'contacts', 'workingHours', 'images', 'lat', 'lon', 'types', 'infoEn', 'infoRu', 'infoKg',
                  'active', 'video', 'cityStr', 'instructionsRu', 'instructionsKg', 'instructionsEn', 'link_zip',
                  'nameStr', 'nameStart', 'stateStr', 'surnameStr', 'email')


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelPackage
        fields = ('id', 'client', 'dateCreated', 'status', 'pid', 'senderCountry', 'senderCity', 'receiverCountry',
                  'receiverCity', 'dateArrived', 'orderNumber', 'packageData', 'packageType', 'paymentStatus',
                  'clientName', 'height', 'width', 'length', 'weight',
                  'clients', 'senderName', 'senderPhone', 'receiverName', 'receiverPhone', 'costPerKg', 'extraCost',
                  'totalCost', 'comment', 'tariff', 'extraServices', 'itemCost', 'quantity')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelItem
        fields = ('id', 'name', 'description', 'category', 'subcategory', 'cost', 'costSale',
                  'issale', 'supplier', 'uniqueid', 'image', 'phone', 'instagram', 'facebook', 'whatsapp', 'web',
                  'likes', 'views', 'imagelink', 'sale_type', 'isoptovik', 'optovikcost', 'priority', 'country', 'city',
                  'sizes', 'colors', 'memory', 'gender_type', 'images', 'descHtml', 'screen')


class TrackNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelRequests
        fields = ('trackNumbers',)


class PackageSerializerGet(serializers.ModelSerializer):
    client = ClientSerializer()
    packageType = PackageTypeSerializer()
    senderCountry = CountrySerializer()
    senderCity = CitySerializer()
    receiverCountry = CountrySerializer()
    receiverCity = CitySerializer()
    packageData = PackageDataSerializer()
    extraServices = ExtraServiceSerializer(many=True, )
    item = ItemSerializer(read_only=True)
    request = TrackNumberSerializer(read_only=True)

    class Meta:
        model = models.ModelPackage
        fields = (
            'id', 'client', 'dateCreated', 'status', 'pid', 'senderCountry', 'senderCity', 'receiverCountry',
            'receiverCity', 'dateArrived', 'orderNumber', 'request', 'packageData', 'packageType', 'paymentStatus',
            'clientName', 'extraServices',
            'clients', 'senderName', 'senderPhone', 'receiverName', 'receiverPhone', 'costPerKg', 'extraCost',
            'customExpenses', 'totalCost', 'comment', 'tariff', 'height', 'width', 'length', 'weight', 'personal',
            'personal_description', 'image', 'item', 'itemCost', 'quantity',
        )


class AlaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelAlaket
        fields = ('id', 'date', 'dateCreated', 'client', 'fromCity', 'toCity', 'title', 'description', 'cost', 'type',
                  'photo', 'flyTime')


class AlaketSerializerGet(serializers.ModelSerializer):
    client = ClientSerializer()
    fromCity = CitySerializer()
    toCity = CitySerializer()

    class Meta:
        model = models.ModelAlaket
        fields = ('id', 'date', 'dateCreated', 'client', 'fromCity', 'toCity', 'title', 'description', 'cost', 'type',
                  'photo', 'flyTime')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelImage
        fields = ('id', 'title', 'image')


class SavePackageSerializer(serializers.Serializer):
    package = serializers.IntegerField()
    clients = serializers.IntegerField()

    class Meta:
        fields = ('package', 'clients')


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelAddresses
        fields = ('id', 'type', 'depot', 'country', 'city', 'address', 'phone', 'receiverName', 'nameAddress', 'user')


class AddressesSerializerGet(serializers.ModelSerializer):
    depot = DepotSerializerGet()
    country = CountrySerializer()
    city = CitySerializer()
    user = ClientSerializer()

    class Meta:
        model = models.ModelAddresses
        fields = ('id', 'type', 'depot', 'country', 'city', 'address', 'phone', 'receiverName', 'nameAddress', 'user')


class AddressesSerializerOpen(serializers.ModelSerializer):
    depot = DepotSerializerGet()
    country = CountrySerializer()
    city = CitySerializer()

    class Meta:
        model = models.ModelAddresses
        fields = ('id', 'type', 'depot', 'country', 'city', 'address', 'phone', 'receiverName', 'nameAddress', 'user')


class PackageRequestSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = models.ModelPackage
        fields = ('personal', 'personal_description', 'image', 'item', 'itemCost', 'quantity',)

    def get_item(self, obj):
        if obj.item:
            return str(obj.item.id)
        return None


class RequestSerializerGet(serializers.ModelSerializer):
    fromCountry = CountrySerializer()
    fromCity = CitySerializer()
    toCountry = CountrySerializer()
    toCity = CitySerializer()
    packageType = PackageTypeSerializer()
    client = ClientSerializer()
    packageData = PackageDataSerializer()
    address = AddressesSerializerOpen()
    package = PackageRequestSerializer()
    file = FileSerializer(many=True, read_only=True)

    class Meta:
        model = models.ModelRequests
        fields = ('id', 'senderName', 'senderPhone', 'receiverName', 'receiverPhone', 'serviceName', 'fromCountry',
                  'fromCity', 'toCountry', 'toCity', 'packageType', 'packageData', 'dateSending',
                  'phone', 'telegram', 'comment', 'client', 'weight', 'archive', 'trackNumbers', 'height', 'width',
                  'cost', 'length', 'dateCreated', 'extraServices', 'premium', 'address', 'package', 'file',
                  'is_private', 'private_item_description', 'product_link')
        read_only_fields = ('id', 'dateCreated')


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ModelRequests
        fields = ('id', 'senderName', 'senderPhone', 'receiverName', 'receiverPhone', 'serviceName', 'fromCountry',
                  'fromCity', 'toCountry', 'toCity', 'packageType', 'packageData', 'dateSending',
                  'phone', 'telegram', 'comment', 'client', 'weight', 'archive', 'trackNumbers', 'height', 'width',
                  'cost', 'length', 'dateCreated', 'extraServices', 'premium', 'address', 'package', 'file', 
                  'is_private', 'private_item_description', 'product_link')
        read_only_fields = ('id', 'dateCreated')

    def create(self, validated_data):
        package_data = validated_data.pop('package', None)
        extra_services_data = validated_data.pop('extraServices', [])
        file = validated_data.pop('file', [])
        request = models.ModelRequests.objects.create(**validated_data)

        # if package_data:
        #     models.ModelPackage.objects.create(request=request, **package_data)
        #     print(type(package_data))

        if extra_services_data:
            request.extraServices.set(extra_services_data)

        # if file:
        #     models.ModelPackage.objects.create(request=request, **file)
        return request

    def update(self, instance, validated_data):
        package_data = validated_data.pop('package', None)
        extra_services_data = validated_data.pop('extraServices', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if package_data:
            if instance.package:
                for attr, value in package_data.items():
                    setattr(instance.package, attr, value)
                instance.package.save()
            else:
                models.ModelPackage.objects.create(request=instance, **package_data)

        if extra_services_data:
            instance.extraServices.set(extra_services_data)

        instance.save()
        return instance

class AcceptedRequestSerializer(serializers.Serializer):
    request_id = serializers.IntegerField(write_only=True)

    class Meta:
        fields = ('request_id', )


class DepotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DepotUser
        fields = ('id', 'login', 'password', 'depot', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', 'user_type')

    def create(self, validated_data):
        depot_user = models.DepotUser.objects.create_user(**validated_data)
        depot_user.set_password(validated_data['password'])
        depot_user.user_type = utils.DEPOT_USER
        depot_user.save()
        return depot_user


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BuyerBanners
        fields = ('id', 'title', 'text', 'photo', 'order')


class CartRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartRequest
        fields = ('comment', 'link', 'itemCost', 'quantity')


class BuyerRequestSerializer(serializers.ModelSerializer):
    cart_request = serializers.ListSerializer(child=CartRequestSerializer(), allow_empty=False)

    class Meta:
        model = models.ModelBuyerRequest
        fields = ('id', 'link', 'phone', 'name', 'client', 'dateCreated', 'status', 'comment', 'cart_request', 'active',
                  'paid', 'totalCost', 'info', 'trackNumbers')

    def create(self, validated_data):
        cart_requests = validated_data.pop('cart_request', None)
        cart_req_id = []
        for i in cart_requests:
            cart_req = models.CartRequest.objects.create(**i)
            cart_req_id.append(cart_req.id)

        buyer_request = models.ModelBuyerRequest.objects.create(**validated_data)
        buyer_request.cart_request.set(cart_req_id)
        buyer_request.save()
        return buyer_request


class BuyerRequestSerializerGet(serializers.ModelSerializer):
    client = ClientSerializer()
    cart_request = CartRequestSerializer(many=True, )

    class Meta:
        model = models.ModelBuyerRequest
        fields = ('id', 'link', 'phone', 'name', 'client', 'dateCreated', 'status', 'comment', 'cart_request', 'active',
                  'paid', 'totalCost', 'info', 'trackNumbers')


class ColorSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelColorSize
        fields = ('size',)


class ItemColorSerializer(serializers.ModelSerializer):
    color_sizes = ColorSizeSerializer(many=True, required=False)

    class Meta:
        model = ModelColor
        fields = ('color', 'color_sizes')


class ItemCreateSerializer(serializers.ModelSerializer):
    colors = ItemColorSerializer(many=True, required=False)

    class Meta:
        model = ModelItem
        fields = ('id', 'name', 'description', 'category', 'subcategory', 'cost', 'costSale',
                  'issale', 'supplier', 'uniqueid', 'image', 'phone', 'instagram', 'facebook', 'whatsapp', 'web',
                  'likes', 'views', 'imagelink', 'sale_type', 'isoptovik', 'optovikcost', 'priority', 'country', 'city',
                  'colors', 'memory', 'gender_type', 'images', 'descHtml', 'screen')

    def to_internal_value(self, data):
        if isinstance(data, QueryDict):
            data = data.copy()
            colors_data = data.get('colors')

            if colors_data:
                try:
                    colors_json = json.loads(colors_data)
                    data['colors'] = [color for color in colors_json]
                except (json.JSONDecodeError, KeyError):
                    raise serializers.ValidationError({
                        'colors': 'Некорректный формат JSON строки в списке.'
                    })

        return super().to_internal_value(data)

    def create(self, validated_data):
        colors_data = validated_data.pop('colors', [])
        memory_data = validated_data.pop('memory', [])

        item = ModelItem.objects.create(**validated_data)

        colors = []
        for color_data in colors_data:
            color = ModelColor.objects.get(pk=color_data['color'])
            color_sizes_data = color_data.pop('color_sizes', [])

            for color_size_data in color_sizes_data:
                ModelColorSize.objects.create(item=item, color=color, **color_size_data)
            colors.append(color.id)

        if colors:
            item.colors.set(colors)
        if memory_data:
            item.memory.set(memory_data)

        return item


class ItemColorTestSerializer(serializers.ModelSerializer):
    color_sizes = ColorSizeSerializer(many=True)

    class Meta:
        model = ModelColor
        fields = ('color', 'image', 'nameRu', 'nameKg', 'nameEn', 'color_sizes')


class ItemTestSerializerOpen(serializers.ModelSerializer):
    supplier = StoreSerializerOpen()
    image = serializers.SerializerMethodField()
    country = CountrySerializer()
    city = CitySerializer()
    category = CategorySerializer()
    subcategory = SubCategorySerializer()
    # colors = ColorSerializer(many=True, allow_null=True)
    memory = MemorySerializer(many=True, allow_null=True)
    screen = MatrixSerializer(allow_null=True)
    colors = ItemColorTestSerializer(many=True)

    class Meta:
        model = models.ModelItem
        fields = ('id', 'name', 'description', 'category', 'subcategory', 'cost', 'costSale',
                  'issale', 'supplier', 'uniqueid', 'image', 'phone', 'instagram', 'facebook', 'whatsapp', 'web',
                  'likes', 'views', 'imagelink', 'sale_type', 'isoptovik', 'optovikcost', 'priority', 'country', 'city',
                  'sizes', 'colors', 'memory', 'gender_type', 'images', 'descHtml', 'screen')

    def get_image(self, store):
        request = self.context.get('request')
        if store.image:
            if request is not None:
                image = store.image.url
                return request.build_absolute_uri(image)
            return store.image.url
        else:
            return store.imagelink


class ItemPatchSerializer(serializers.ModelSerializer):
    colors = ItemColorSerializer(many=True)

    class Meta:
        model = models.ModelItem
        fields = ('id', 'name', 'description', 'category', 'subcategory', 'cost', 'costSale',
                  'issale', 'supplier', 'uniqueid', 'image', 'phone', 'instagram', 'facebook', 'whatsapp', 'web',
                  'likes', 'views', 'imagelink', 'sale_type', 'isoptovik', 'optovikcost', 'priority', 'country', 'city',
                  'colors', 'memory', 'gender_type', 'descHtml', 'screen')

    def get_image(self, store):
        request = self.context.get('request')
        if store.image:
            if request is not None:
                image = store.image.url
                return request.build_absolute_uri(image)
            return store.image.url
        else:
            return store.imagelink


class ItemSerializerOpen(serializers.ModelSerializer):
    supplier = StoreSerializerOpen()
    image = serializers.SerializerMethodField()
    country = CountrySerializer()
    city = CitySerializer()
    category = CategorySerializer()
    subcategory = SubCategorySerializer()
    colors = ColorSerializer(many=True, allow_null=True)
    memory = MemorySerializer(many=True, allow_null=True)
    screen = MatrixSerializer(allow_null=True)
    # colors = ItemColorSerializer(many=True)

    class Meta:
        model = models.ModelItem
        fields = ('id', 'name', 'description', 'category', 'subcategory', 'cost', 'costSale',
                  'issale', 'supplier', 'uniqueid', 'image', 'phone', 'instagram', 'facebook', 'whatsapp', 'web',
                  'likes', 'views', 'imagelink', 'sale_type', 'isoptovik', 'optovikcost', 'priority', 'country', 'city',
                  'sizes', 'colors', 'memory', 'gender_type', 'images', 'descHtml', 'screen')

    def get_image(self, store):
        request = self.context.get('request')
        if store.image:
            if request is not None:
                image = store.image.url
                return request.build_absolute_uri(image)
            return store.image.url
        else:
            return store.imagelink


class GetItemSerializer(serializers.ModelSerializer):
    """Serializer for Item"""

    class Meta:
        model = models.ModelItem
        fields = (
            'id', 'name', 'description', 'category', 'subcategory',
            'cost', 'costSale', 'issale', 'supplier', 'uniqueid', 'image', 'phone',
            'imagelink', 'instagram', 'facebook', 'whatsapp', 'web', 'likes', 'views', 'isoptovik',
            'optovikcost', 'priority'
            )

        read_only_fields = ('id',)
        depth = 1


class CartItemSerializer(serializers.ModelSerializer):
    """Serializer for cart items"""
    class Meta:
        model = models.CartItems
        fields = (
            'id', 'item', 'quantity', 'color', 'size', 'memory'
        )
        read_only_fields = ('id', )


class CartItemSerializerGet(serializers.ModelSerializer):
    """Serializer for cart items"""
    item = GetItemSerializer()

    class Meta:
        model = models.CartItems
        fields = (
            'id', 'item', 'quantity', 'color', 'size', 'memory'
        )
        read_only_fields = ('id', )


class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = models.ModelOrder
        fields = (
            'id', 'items', "store", "totalCost", "user", 'addresses', 'phone', 'lat', 'lon',
            'comment', 'storeName', 'storeLogo', 'status', 'date', 'isoptovik', 'bonus', 'pay_status', 'client'
        )

    def create(self, validated_data):

        items = validated_data.pop("items", None)
        order = models.ModelOrder.objects.create(**validated_data)
        cart_items_id = []
        if items:
            for i in items:
                cart_item = models.CartItems.objects.create(**i)
                cart_items_id.append(cart_item.id)
        order.items.set(cart_items_id)
        return order

    # def update(self, instance, validated_data):
    #     items = validated_data.pop("items", None)
    #     cart_items_id = []
    #     if items:
    #         for i in items:
    #             cart_item = models.CartItems.objects.create(**i)
    #             cart_items_id.append(cart_item.id)
    #     instance.items.set(cart_items_id)
    #     return instance


class OrderSerializerGet(serializers.ModelSerializer):
    items = CartItemSerializerGet(many=True, required=False, allow_null=True)
    client = ClientSerializer()
    addresses = AddressesSerializer()

    class Meta:
        model = models.ModelOrder
        fields = (
            'id', 'items', "store", "totalCost", "user", 'addresses', 'phone', 'lat', 'lon',
            'comment', 'storeName', 'storeLogo', 'status', 'date', 'isoptovik', 'bonus', 'pay_status', 'client'
        )

    def create(self, validated_data):

        items = validated_data.pop("items", None)
        order = models.ModelOrder.objects.create(**validated_data)

        if items:
            for i in items:
                models.CartItems.objects.create(order=order, **i)
        return order


class DataSerializer(serializers.Serializer):
    category = CategorySerializer()
    items = serializers.ListSerializer(child=ItemSerializer(), allow_empty=False)

    class Meta:
        fields = ('category', 'items')


class FiveItemSerializer(serializers.Serializer):
    data = serializers.ListSerializer(child=DataSerializer(), allow_empty=False)

    class Meta:
        fields = ('data', )


class FiveItemSerializerData(serializers.Serializer):
    items = serializers.ListSerializer(child=ItemSerializer(), allow_empty=False)

    class Meta:
        fields = ('items', )


class GetItemByIDSerializer(serializers.Serializer):
    items_id = serializers.ListSerializer(child=serializers.IntegerField(), allow_empty=False)

    class Meta:
        fields = ('items_id', )


class WantedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WantedItems
        fields = ('id', 'description', 'photo')


class ItemSearchRequestSerializer(serializers.ModelSerializer):
    wantedItems = serializers.ListSerializer(child=WantedItemsSerializer(), allow_empty=False)

    class Meta:
        model = models.ModelItemSearchRequest
        fields = ('id', 'client', 'name', 'phone', 'wantedItems', 'active', 'description')

    def create(self, validated_data):
        wanted_items = validated_data.pop('wantedItems', None)
        wan_items_id = []
        for i in wanted_items:
            wan_item = models.WantedItems.objects.create(**i)
            wan_items_id.append(wan_item.id)

        item_search_request = models.ModelItemSearchRequest.objects.create(**validated_data)
        item_search_request.wantedItems.set(wan_items_id)
        item_search_request.save()
        return item_search_request


class ItemSearchRequestSerializerGet(serializers.ModelSerializer):
    client = ClientSerializer()
    wantedItems = WantedItemsSerializer(many=True, )

    class Meta:
        model = models.ModelItemSearchRequest
        fields = ('id', 'client', 'name', 'phone', 'wantedItems', 'active', 'description')


class SetSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100,)

    class Meta:
        fields = ('code', )


class CryptoPaymentListSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)

    class Meta:
        model = models.CryptoPay
        fields = [
            'id',
            'client',
            'wallet',
            'payment_type',
            'transaction_hash',
            'send_receipt',
            'receipt_email',
            'payment_status',
            'created_at',
            'is_paid',
        ]



class CryptoPaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CryptoPay
        fields = [
            'client',
            'wallet',
            'payment_type',
            'transaction_hash',
            'send_receipt',
            'receipt_email',
            'payment_status',
            'created_at',
            'is_paid',
        ]
    def create(self, validated_data):
        validated_data['payment_status'] = 'waiting'
        return super().create(validated_data)

class TariffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TariffList
        fields = ('id', 'weight', 'price',)

class TariffScheduleSerializer(serializers.ModelSerializer):
    tariff = TariffListSerializer(many=True)
    class Meta:
        model = models.TariffSchedule
        fields = ('id', 'tariff',)
        ref_name = "TariffSerializerForSchedule"


class TariffSerializer(serializers.ModelSerializer):
    tariff_schedule = TariffScheduleSerializer(read_only=True)
    class Meta:
        model = models.ModelDepots
        fields = ('id', 'tariff_schedule',)
        ref_name = "TariffScheduleSerializerForDepot"
