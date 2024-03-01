# Generated by Django 5.0.1 on 2024-01-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "sobrenome",
                    models.CharField(max_length=100, verbose_name="Sobrenome"),
                ),
                ("email", models.EmailField(max_length=100, verbose_name="E-mail")),
            ],
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
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "preco",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Preço"
                    ),
                ),
                ("estoque", models.IntegerField(verbose_name="Qtde em estoque")),
            ],
        ),
    ]
