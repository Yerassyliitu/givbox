from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.templatetags.rest_framework import data
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from category.models import Category
from category.serializers import CountrySerializer, CitySerializer, WebsiteSerializer, StoreCategorySerializer, \
    ContactsSerializer, CategorySerializer, NotificationSerializer
from user import models, utils
from user.models import Client

User = get_user_model()


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelWallet
        fields = ('id', 'client_name', 'amount')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('id', 'login', 'password', 'phone', 'fullname', 'address', 'avatar', 'country', 'city', 'wallet',
                  'passport_front', 'passport_back', 'isVerified', 'dateCreated', 'user_type', 'inn', 'isVip')
        extra_kwargs = {'password': {'write_only': True}}


class ClientSerializerGet(serializers.ModelSerializer):
    country = CountrySerializer()
    city = CitySerializer()
    wallet = WalletSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = models.Client
        fields = ('id', 'login', 'password', 'phone', 'fullname', 'address', 'avatar', 'country', 'city', 'wallet',
                  'user_type', 'passport_front', 'passport_back', 'isVerified', 'dateCreated', 'inn', 'isVip')
        read_only_fields = ('user_type', 'id')
        extra_kwargs = {'password': {'write_only': True}}


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id', 'login', 'password', 'fullname', 'phone', 'active')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        employee = models.Employee.objects.create_user(**validated_data)
        employee.set_password(validated_data['password'])
        employee.save()
        return employee


class WalletHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelWalletHistory
        fields = ('id', 'date', 'amount', 'client', 'description')


class WalletHistorySerializerGet(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = models.ModelWalletHistory
        fields = ('id', 'date', 'amount', 'client', 'description')


class WalletAmountModifySerializer(serializers.Serializer):
    amount = serializers.FloatField()
    description = serializers.CharField(max_length=256)

    class Meta:
        fields = ('amount', 'description')


class WalletAmountModifyResponse(serializers.Serializer):
    message = serializers.CharField(max_length=20)

    class Meta:
        fields = ('message', )


class LoginSerializer(serializers.ModelSerializer):
    """Serializer for login"""
    login = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False
    )

    class Meta:
        model = User
        fields = ('login', 'password')

    def validate(self, data):
        login = data.get('login')
        password = data.get('password')

        if login is None:
            raise serializers.ValidationError(
                'A phone or email is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(
            request=self.context.get('request'),
            login=login,
            password=password,
        )

        if not user:
            msg = ('Неправильный логин или пароль')
            raise serializers.ValidationError({'detail': msg}, code='authorization')

        data['user'] = user

        return data


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BuyerUser
        fields = ('id', 'fullname', 'passportNo', 'info', 'avatar', 'phone', 'login', 'password', 'user_type',
                  'countries', 'websites', 'passport_front', 'passport_back', 'experience', 'commission', 'paymentType',
                  'search_product', 'contacts', 'country', 'redemption_speed', 'email', 'insta', 'instaLink', 'face',
                  'faceLink', 'tg', 'tgLink', 'whatsApp', 'whatsAppLink')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', 'user_type')

    def create(self, validated_data):
        countries = validated_data.pop('countries', None)
        websites = validated_data.pop('websites', None)
        buyer = models.BuyerUser.objects.create_user(**validated_data)
        buyer.set_password(validated_data['password'])
        buyer.user_type = utils.BUYER
        buyer.countries.set(countries)
        buyer.websites.set(websites)
        buyer.save()
        return buyer


class BuyerSerializerGet(serializers.ModelSerializer):
    countries = CountrySerializer(many=True, )
    websites = WebsiteSerializer(many=True, )
    contacts = ContactsSerializer()
    country = CountrySerializer()

    class Meta:
        model = models.BuyerUser
        fields = ('id', 'fullname', 'passportNo', 'info', 'avatar', 'phone', 'login', 'password', 'user_type',
                  'countries', 'websites', 'passport_front', 'passport_back', 'experience', 'commission', 'paymentType',
                  'search_product', 'contacts', 'country', 'redemption_speed', 'email', 'insta', 'instaLink', 'face',
                  'faceLink', 'tg', 'tgLink', 'whatsApp', 'whatsAppLink')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', 'user_type')


class SupportUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SupportUsers
        fields = ('id', 'login', 'password', 'avatar', 'phone', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', 'user_type')

    def create(self, validated_data):
        support_user = models.SupportUsers.objects.create_user(**validated_data)
        support_user.set_password(validated_data['password'])
        support_user.user_type = utils.SUPPORT_USER
        support_user.save()
        return support_user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['fullname'] = user.fullname
        token['login'] = user.login
        token['user_type'] = user.user_type
        # ...

        return token


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = ('id', 'fullname', 'login', 'phone', 'avatar', 'email', 'address', 'location', 'longitude', 'latitude',
                  'instagram', 'facebook', 'whatsapp', 'web', 'slogan', 'description', 'rating', 'storeCategory',
                  'priority', 'sale_type', 'visibility')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        categories = validated_data.pop('storeCategory', None)
        password = validated_data.pop('password', None)
        store = models.Store.objects.create_user(**validated_data)
        store.set_password(password)
        store.storeCategory.set(categories)
        store.save()
        return store


class StoreSerializerGet(serializers.ModelSerializer):
    storeCategory = StoreCategorySerializer(many=True, )

    class Meta:
        model = models.Store
        fields = ('id', 'fullname', 'login', 'phone', 'avatar', 'email', 'address', 'location', 'longitude', 'latitude',
                  'instagram', 'facebook', 'whatsapp', 'web', 'slogan', 'description', 'rating', 'storeCategory',
                  'priority', 'sale_type', 'visibility')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        categories = validated_data.pop('storeCategory', None)
        store = models.Store.objects.create_user(**validated_data)
        store.set_password(validated_data['password'])
        store.storeCategory.set(categories)
        store.save()
        return store


class StoreSerializerOpen(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = ('id', 'fullname', 'avatar')


class CategorySerializerGet(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField(allow_null=True, )
    store = StoreSerializerOpen(many=True, required=False, allow_null=True)

    class Meta:
        model = Category
        fields = ('id', 'nameEn', 'nameRus', 'nameKg', 'icon', 'priority', 'isoptovik', 'store')

    def get_icon(self, category):
        request = self.context.get('request')
        if request is not None:
            try:
                icon = category.icon.url
                return request.build_absolute_uri(icon)
            except:
                return ""
        return category.icon


class BecomeBuyerSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer()

    class Meta:
        model = models.ModelBecomeBuyer
        fields = ('id', 'client', 'passport_front', 'passport_back', 'comment', 'accepted', 'dateCreated', 'fullname',
                  'about_yourself', 'experience', 'commission', 'redemption_speed', 'country', 'shop_countries',
                  'paymentType', 'search_product', 'rating', 'contacts', 'redemption_speed', 'email', 'insta',
                  'instaLink', 'face', 'faceLink', 'tg', 'tgLink', 'whatsApp', 'whatsAppLink')

    def create(self, validated_data):
        contact = validated_data.pop('contacts', None)
        shop_countries = validated_data.pop('shop_countries', None)
        buyer = models.ModelBecomeBuyer.objects.create(**validated_data)
        buyer.shop_countries.set(shop_countries)
        contact_ob = models.ModelContact.objects.create(**contact)
        buyer.contacts = contact_ob
        buyer.save()
        return buyer


class BecomeBuyerSerializerGet(serializers.ModelSerializer):
    client = ClientSerializer()
    contacts = ContactsSerializer()
    shop_countries = CountrySerializer(many=True, )
    country = CountrySerializer()

    class Meta:
        model = models.ModelBecomeBuyer
        fields = ('id', 'client', 'passport_front', 'passport_back', 'comment', 'accepted', 'dateCreated', 'fullname',
                  'about_yourself', 'experience', 'commission', 'redemption_speed', 'country', 'shop_countries',
                  'paymentType', 'search_product', 'rating', 'contacts', 'redemption_speed', 'email', 'insta',
                  'instaLink', 'face', 'faceLink', 'tg', 'tgLink', 'whatsApp', 'whatsAppLink')


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelShopUser
        fields = ('id', 'login', 'password', 'fullname', 'dateRegistered')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('dateRegistered', 'id')

    def create(self, validated_data):
        shop_user = models.ModelShopUser.objects.create_user(**validated_data)
        shop_user.set_password(validated_data['password'])
        shop_user.save()
        return shop_user


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email',)


class PasswordResetRequestResponse(serializers.Serializer):
    message = serializers.CharField(max_length=2)

    class Meta:
        fields = ('message', )


class PasswordResetSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

    class Meta:
        fields = ('code', )


class PasswordResetResponse(serializers.Serializer):
    token = serializers.CharField(max_length=200)
    data = serializers.IntegerField(help_text='User ID')

    class Meta:
        fields = ('token', 'data')


class ChangePasswordWithoutOldPasswordSerializer(serializers.Serializer):
    models = User

    new_password = serializers.CharField(required=True)
    user_id = serializers.CharField(required=True)


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    user_id = serializers.CharField(required=True)


class EmailConfirmationRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email', )


class EmailConfirmationSerializer(serializers.Serializer):
    confirm_code = serializers.CharField(max_length=6)

    class Meta:
        fields = ('confirm_code', )


class UserNotificationSerializer(serializers.ModelSerializer):
    notifications = NotificationSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = (
            'id', 'notifications',
        )
