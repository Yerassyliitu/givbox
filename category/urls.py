from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'category'

router = SimpleRouter()

router.register(r'hour_work', views.HourWorkViewSet)
router.register(r'contact', views.ContactsViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'city', views.CityViewSet)
router.register(r'packageType', views.PackageTypeViewSet)
router.register(r'notification', views.NotificationViewSet)
router.register(r'costs', views.CostsViewSet)
router.register(r'tariff', views.TariffViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'website', views.WebsiteViewSet)
router.register(r'store_category', views.StoreCategoryViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'sub_category', views.SubCategoryViewSet)
router.register(r'franchise', views.FranchiseViewSet)
router.register(r'businessRequest', views.BusinessRequestViewSet)
router.register(r'files', views.FileViewSet)
router.register(r'extra_service', views.ExtraServiceViewSet)
router.register(r'color', views.ColorViewSet)
router.register(r'memory', views.MemoryViewSet)
router.register(r'matrix', views.MatrixViewSet)
router.register(r'currencyFromUSD', views.CurrencyFromUSDViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
