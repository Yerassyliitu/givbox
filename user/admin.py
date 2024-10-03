from django.contrib import admin
from user import models, utils
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.db.models import QuerySet


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ('login', 'name', 'phone',)
    search_fields = ['login']
    list_filter = (
    )

    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        (_('Personal info'), {'fields': ('name', 'phone', 'address', 'avatar', 'user_type', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2')
        }),
    )

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        obj.save()


@admin.action(description='Создать кошелек')
def create_wallet(self, request, qs:QuerySet):
    clients = qs.all()
    for client in clients:
        wallet = models.ModelWallet.objects.create(client_name=client.fullname, currency=utils.DOLLAR, amount=0)
        client.wallet.add(wallet)


class ClientAdmin(admin.ModelAdmin):
    search_fields = ('fullname',)
    list_display = ['id', 'login', 'fullname']
    actions = [create_wallet]

    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        (_('Personal info'), {'fields': ('fullname', 'phone', 'address', 'avatar', 'country', 'city', 'wallet',
                                         'isVip')}),
    )

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        obj.save()


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('fullname', )
    list_display = ['id', 'login', 'fullname']

    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        (_('Personal info'), {'fields': ('fullname', 'phone', 'active')}),
    )

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        obj.save()


class BuyerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        (_('Personal info'), {'fields': ('fullname', 'passportNo', 'info', 'avatar', 'phone', 'user_type', 'countries',
                                         'websites', 'passport_front', 'passport_back', 'country', 'redemption_speed',
                                         'email', 'insta', 'instaLink', 'face', 'faceLink', 'tg', 'tgLink', 'whatsApp',
                                         'whatsAppLink')}),
    )
    readonly_fields = ('user_type',)

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        obj.save()


class SupportAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        (_('Personal info'), {'fields': ('fullname', 'avatar', 'phone', 'user_type')}),
    )
    readonly_fields = ('user_type',)

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        obj.save()


class StoreAdmin(admin.ModelAdmin):
    search_fields = ('fullname',)
    list_display = ['id', 'login', 'fullname']
    actions = [create_wallet]

    fieldsets = (
        (_('Personal info'), {'fields': (
            'fullname', 'login', 'phone', 'avatar', 'email', 'address', 'location', 'longitude', 'latitude',
            'instagram', 'facebook', 'whatsapp', 'web', 'slogan', 'description', 'rating', 'storeCategory',
            'priority', 'sale_type', 'visibility'
        )}),
    )

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        obj.save()


class WalletAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'amount']


admin.site.register(models.ModelWallet, WalletAdmin)
admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Employee, EmployeeAdmin)
admin.site.register(models.ModelWalletHistory)
admin.site.register(models.BuyerUser, BuyerAdmin)
admin.site.register(models.SupportUsers, SupportAdmin)
admin.site.register(models.Store, StoreAdmin)
admin.site.register(models.ModelBecomeBuyer)

