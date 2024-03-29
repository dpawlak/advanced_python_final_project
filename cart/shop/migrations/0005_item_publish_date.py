# Generated by Django 4.2.1 on 2023-05-05 19:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_alter_transaction_quantity_of_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="publish_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date published"
            ),
            preserve_default=False,
        ),
    ]
