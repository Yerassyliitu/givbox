from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'user'

router = SimpleRouter()

router.register(r'wallet', views.WalletViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'wallet_history', views.WalletHistoryViewSet)
router.register(r'buyer', views.BuyerViewSet)
router.register(r'support_user', views.SupportUserViewSet)
router.register(r'store', views.StoreViewSet)
router.register(r'becomeBuyer', views.BecomeBuyerViewSet)
router.register(r'shop_user', views.ShopUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('wallet_amount_modify/<int:pk>/', views.WalletAmountModifyView.as_view()),
    path('password/reset-request/', RequestPasswordResetView.as_view()),
    path('password/reset/', ValidateResetCodeView.as_view()),
    path('change-password/without_old_password/', ChangePasswordWithoutOldPasswordView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('emailConfirmation_request/', views.EmailConfirmationRequestViewSet.as_view()),
    path('emailConfirmation/', views.EmailConfirmationViewSet.as_view())
]
