# Generated by Django 4.2.1 on 2023-05-05 19:33

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_transaction_delete_date_delete_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="quantity_of_item",
            field=models.IntegerField(default=0, verbose_name=shop.models.Item),
        ),
    ]
