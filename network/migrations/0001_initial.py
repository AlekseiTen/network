# Generated by Django 5.1.6 on 2025-02-11 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NetworkNode",
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
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Название звена сети"
                    ),
                ),
                (
                    "contact_email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                ("city", models.CharField(max_length=100, verbose_name="Город")),
                ("street", models.CharField(max_length=255, verbose_name="Улица")),
                (
                    "house_number",
                    models.CharField(max_length=20, verbose_name="Номер дома"),
                ),
                (
                    "level",
                    models.IntegerField(
                        choices=[
                            (0, "Завод"),
                            (1, "Розничная сеть"),
                            (2, "Индивидуальный предприниматель"),
                        ],
                        verbose_name="Уровень в сети",
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        verbose_name="Задолженность",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "supplier_node",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="clients",
                        to="network.networknode",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Звено в сети(поставщик)",
                "verbose_name_plural": "Звенья в сети(поставщики)",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название продукта"),
                ),
                ("model", models.CharField(max_length=255, verbose_name="Модель")),
                ("release_date", models.DateField(verbose_name="Дата выхода на рынок")),
                (
                    "network_node",
                    models.ManyToManyField(
                        related_name="products",
                        to="network.networknode",
                        verbose_name="Узел сети",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["-release_date"],
            },
        ),
    ]
