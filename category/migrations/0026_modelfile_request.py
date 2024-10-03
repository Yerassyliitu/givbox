# Generated by Django 4.1.13 on 2024-09-17 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0059_cryptopay_receipt_email_cryptopay_send_receipt_and_more"),
        ("category", "0025_modelnotification_client"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelfile",
            name="request",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="file",
                to="core.modelrequests",
            ),
        ),
    ]
