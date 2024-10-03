from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import CryptoPay
from core.utils import CRYPTO_PAID


@receiver(post_save, sender=CryptoPay)
def update_package_status(sender, instance, created, **kwargs):
    if not created and instance.payment_status == 'paid':
        instance.package.paymentStatus = CRYPTO_PAID
        instance.package.save()