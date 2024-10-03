from django.urls import path, include

from . import views
from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'core'

router = SimpleRouter()

router.register(r'depot', views.DepotViewSet)
router.register(r'package', views.PackageViewSet)
router.register(r'alaket', views.AlaketViewSet)
router.register(r'image', views.ImageViewSet)
router.register(r'request', views.RequestViewSet)
router.register(r'depot_user', views.DepotUserViewSet)
router.register(r'package_data', views.PackageDataViewSet)
router.register(r'addresses', views.AddressesViewSet)
router.register(r'banners', views.BannersViewSet)
router.register(r'buyer_request', views.BuyerRequestViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'item_test', views.ItemCreateViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'item_search_request', views.ItemSearchRequestViewSet)
router.register(r'crypto_payment', views.CryptoPaymentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('savePackage/', views.SavePackageViewSet.as_view()),
    path('accepted_request/', views.AcceptedRequestViewSet.as_view()),
    path('five_item/', views.GetItemViewSet.as_view()),
    path('get_items/', views.ItemByIDViewSet.as_view()),
    # path('set_country/', views.SetPhotoAndSizeViewSet.as_view())
    path('set_size/', views.SetSizeViewSet.as_view()),
    path('currency_conversion/', views.CurrencyConversionView.as_view()),
    path('tariff/<int:pk>/', views.TariffScheduleView.as_view()),
]
