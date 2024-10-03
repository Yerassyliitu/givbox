# Generated by Django 4.1.13 on 2024-09-06 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0052_modelpackage_personal"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelpackage",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.modelitem",
                verbose_name="Товар",
            ),
        ),
        migrations.AddField(
            model_name="modelpackage",
            name="personal_description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание личной вещи"
            ),
        ),
        migrations.AlterField(
            model_name="modelpackage",
            name="paymentStatus",
            field=models.CharField(
                choices=[
                    ("paid", "Оплачено"),
                    ("unpaid", "Не оплачено"),
                    ("Оплачено криптой", "Оплачено криптой"),
                ],
                default="unpaid",
                max_length=20,
                verbose_name="Статус оплаты",
            ),
        ),
    ]
