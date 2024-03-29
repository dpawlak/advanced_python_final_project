# Generated by Django 4.2.1 on 2023-05-07 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_item_publish_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="item",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="shop.item"
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="quantity_of_item",
            field=models.IntegerField(default=1),
        ),
    ]
