# Generated by Django 4.2.1 on 2023-05-11 01:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0002_alter_reviews_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="status",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="transaction",
            name="transaction_id",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="reviews",
            name="rating",
            field=models.IntegerField(
                default=5,
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="purchase_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name="TransactionItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(blank=True, default=0, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "item",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="shop.item",
                    ),
                ),
                (
                    "transaction",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="shop.transaction",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Purchaser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
