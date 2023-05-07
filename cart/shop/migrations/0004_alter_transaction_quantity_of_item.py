# Generated by Django 4.2.1 on 2023-05-05 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_alter_transaction_quantity_of_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="quantity_of_item",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="shop.item"
            ),
        ),
    ]
