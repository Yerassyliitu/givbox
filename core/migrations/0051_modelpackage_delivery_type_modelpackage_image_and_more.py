# Generated by Django 4.1.13 on 2024-09-02 09:14

import category.imggenerate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0050_alter_modelpackage_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelpackage",
            name="delivery_type",
            field=models.CharField(
                choices=[
                    ("CDEK", "СДЭК"),
                    ("YANDEX", "Яндекс доставка"),
                    ("OTHER", "Другая транспортная доставка"),
                ],
                default="Другая транспортная доставка",
                max_length=100,
                verbose_name="Тип доставки",
            ),
        ),
        migrations.AddField(
            model_name="modelpackage",
            name="image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=category.imggenerate.all_image_file_path,
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="modelbuyerrequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("CREATED", "Создано"),
                    ("confirmed", "Подтверждено"),
                    ("in_progress", "В процессе"),
                    ("bought", "Куплено"),
                    ("sent", "Отправлено"),
                ],
                default="CREATED",
                max_length=50,
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="modelpackage",
            name="status",
            field=models.CharField(
                choices=[
                    ("CREATED", "Создан"),
                    ("RECEIVED_AT_WAREHOUSE", "Получен на складе"),
                    ("SENT", "Отправлен"),
                    ("ON_WAY", "В пути"),
                    ("ARRIVED_TRANSIT_COUNTRY", "Прибыл в транзитную страну"),
                    ("SENT_TO_DESTINATION_COUNTRY", "Отправлен в страну назначения"),
                    ("ON_WAY_TO_DESTINATION", "В пути"),
                    ("ARRIVED_DESTINATION_COUNTRY", "Прибыл в страну назначения"),
                    ("CUSTOMS_CLEARANCE", "Проходит таможенное оформление"),
                    (
                        "RECEIVED_AT_DESTINATION_WAREHOUSE",
                        "Получен на складе страны назначения",
                    ),
                    ("DELIVERED_TO_RECIPIENT", "Отправлен адресату"),
                ],
                default="CREATED",
                max_length=100,
                verbose_name="Статус",
            ),
        ),
    ]
