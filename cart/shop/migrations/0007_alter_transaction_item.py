# Generated by Django 4.2.1 on 2023-05-07 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_transaction_item_alter_transaction_quantity_of_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="shop.item"
            ),
        ),
    ]
