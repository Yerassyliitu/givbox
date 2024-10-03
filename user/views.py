from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from user import models, serializers, filters, utils
from user.models import User, ModelWallet
from user.serializers import PasswordResetRequestSerializer, PasswordResetRequestResponse, PasswordResetSerializer, \
    PasswordResetResponse
import random

from django.conf import settings
from django.core.mail import send_mail


class WalletViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelWallet.objects.all()
    serializer_class = serializers.WalletSerializer


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClientFilters
    search_fields = ('fullname', 'login', 'phone', 'address', 'country__nameRu', 'country__nameEn', 'country__nameKg', 'city__nameKg', 'city__nameRu', 'city__nameEn')

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.ClientSerializerGet
        else:
            return serializers.ClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = serializers.ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        saved_data = serializer.save()
        user = models.Client.objects.get(pk=saved_data.id)
        user.set_password(request.data['password'])
        user.user_type = utils.CLIENT
        wallet = ModelWallet.objects.create(client_name=user.fullname, currency=utils.DOLLAR, amount=0)
        user.wallet.add(wallet)
        user.save()
        info = models.Client.objects.filter(login=request.data['login'])
        userData = serializers.ClientSerializer(info, many=True)
        refresh = RefreshToken.for_user(user)
        email = user.login
        send_mail(
            subject=f'Добро пожаловать в GivBox {user.fullname} !',
            message='Вы успешно зарегистрировались в платформе GivBox.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token),
                         'data': userData.data}, status=200)


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EmployeeFilter


class WalletHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelWalletHistory.objects.all()
    serializer_class = serializers.WalletHistorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.WalletHistoryFilter

    def get_queryset(self):
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.WalletHistorySerializerGet
        else:
            return serializers.WalletHistorySerializer


class WalletAmountModifyView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    @swagger_auto_schema(request_body=serializers.WalletAmountModifySerializer(),
                         responses={200: serializers.WalletAmountModifyResponse()})
    def post(self, request, pk, format=None):
        user = models.Client.objects.filter(pk=pk).first()
        serializer = serializers.WalletAmountModifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        error = ValidationError({'error': ['Client with this ID does not exists!']})
        if user:
            wallets = user.wallet.all()
            wallet = models.ModelWallet.objects.filter(pk=wallets[0].id).first()
            wallet.amount += data['amount']
            wallet.amount = round(wallet.amount, 1)
            wallet.save()
            wallet_history = models.ModelWalletHistory.objects.create(amount=data['amount'], client=user,
                                                                      description=data['description'])
            wallet_history.save()
            return Response(serializers.WalletAmountModifyResponse({'message': 'success'}).data)
        else:
            raise error


class BuyerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = models.BuyerUser.objects.all()
    serializer_class = serializers.BuyerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.BuyerFilter
    search_fields = ('fullname', )

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.BuyerSerializerGet
        else:
            return serializers.BuyerSerializer


class SupportUserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = models.SupportUsers.objects.all()
    serializer_class = serializers.SupportUserSerializer


class StoreViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = models.Store.objects.all()
    serializer_class = serializers.StoreSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.StoreFilter
    ordering_fields = ('priority',)
    search_fields = ('fullname', 'description', 'slogan')
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.StoreSerializerGet
        else:
            return serializers.StoreSerializer


class BecomeBuyerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = models.ModelBecomeBuyer.objects.all()
    serializer_class = serializers.BecomeBuyerSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.BecomeBuyerSerializerGet
        else:
            return serializers.BecomeBuyerSerializer


class ShopUserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = models.ModelShopUser.objects.all()
    serializer_class = serializers.ShopUserSerializer


class RequestPasswordResetView(APIView):
    authentication_classes = []
    permission_classes = (permissions.AllowAny, )

    @swagger_auto_schema(request_body=PasswordResetRequestSerializer(), responses={200: PasswordResetRequestResponse()})
    def post(self, request, format=None):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recovery_email = serializer.validated_data.get('email')
        user = User.objects.filter(login=recovery_email).first()
        if not user:
            raise ValidationError({'email': ['Пользователь с такой электронной почтой не существует!']})
        from django.utils.crypto import get_random_string
        code = random.randint(100_000, 999_999)
        while User.objects.filter(reset_code=code).exists():
            code = random.randint(100_000, 999_999)
        user.reset_code = code
        send_mail(
            subject='Сброс пароля',
            message=f'Код для сброса пароля: {user.reset_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recovery_email],
            fail_silently=False,
        )
        user.save()
        return Response(PasswordResetRequestResponse({'message': 'ok'}).data)


class ValidateResetCodeView(APIView):
    permission_classes = (permissions.AllowAny, )
    authentication_classes = []

    @swagger_auto_schema(request_body=PasswordResetSerializer(), responses={200: PasswordResetResponse()})
    def post(self, request, format=None):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        user = User.objects.filter(reset_code=code).first()
        error = ValidationError({'error': ['Incorrect code']})
        if not user:
            raise error
        if user.reset_code == code:
            user.reset_code = ''
            user.save()
            refresh = RefreshToken.for_user(user)
            return Response(PasswordResetResponse({
                'token': refresh.access_token,
                'data': user.id,
            }).data)
        else:
            raise error


class ChangePasswordWithoutOldPasswordView(generics.UpdateAPIView):
    serializer_class = serializers.ChangePasswordWithoutOldPasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user_id = User.objects.get(pk=serializer.data.get('user_id'))
            self.object = user_id
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = serializers.ChangePasswordSerializer

    model = User
    permission_classes = (IsAuthenticated, )

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user_id = User.objects.get(pk=serializer.data.get('user_id'))
            self.object = user_id
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailConfirmationRequestViewSet(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=serializers.EmailConfirmationRequestSerializer())
    def post(self, request, format=None):
        serializer = serializers.EmailConfirmationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        confirmable_email = serializer.validated_data.get('email')
        user = User.objects.filter(login=confirmable_email).first()
        # if user:
        #     raise ValidationError({'email': ['Пользователь с такой электронной почтой существует!']})
        code = random.randint(100_000, 999_999)
        while models.ConfirmEmailModel.objects.filter(confirm_code=code).exists():
            code = random.randint(100_000, 999_999)
        confirmable_email_object = models.ConfirmEmailModel.objects.create(email=confirmable_email, confirm_code=code)
        send_mail(
            subject='Подтверждение электронной почты',
            message=f'Код для подтверждение: {confirmable_email_object.confirm_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[confirmable_email_object.email],
            fail_silently=False,
        )
        return Response(PasswordResetRequestResponse({'message': 'ok'}).data)


class EmailConfirmationViewSet(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    @swagger_auto_schema(request_body=serializers.EmailConfirmationSerializer())
    def post(self, request, format=None):
        serializer = serializers.EmailConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('confirm_code')
        confirmable_email_object = models.ConfirmEmailModel.objects.filter(confirm_code=code)
        error = ValidationError({'error': ['Incorrect code']})
        if not confirmable_email_object:
            raise error
        response_email = confirmable_email_object.first().email
        confirmable_email_object.delete()
        return Response({'message': 'Correct code', 'email': f'{response_email}'}, status=200)
