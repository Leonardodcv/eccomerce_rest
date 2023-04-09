# Generated by Django 4.1.7 on 2023-04-09 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0004_remove_historicalindicator_category_product_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalProduct",
            fields=[
                ("id", models.IntegerField(blank=True, db_index=True)),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de eliminacion"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=150, verbose_name="Nombre de Producto"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Descripcion del producto"
                    ),
                ),
                (
                    "image",
                    models.TextField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Imagen del producto",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "category_product",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="products.categoryproduct",
                        verbose_name="Categoria del producto",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "measure_unit",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="products.measureunit",
                        verbose_name="Unidad de medida",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Producto",
                "verbose_name_plural": "historical Productos",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalMeasureUnit",
            fields=[
                ("id", models.IntegerField(blank=True, db_index=True)),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de eliminacion"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        db_index=True, max_length=50, verbose_name="Descripcion"
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Unidad de Medida",
                "verbose_name_plural": "historical Unidades de Medida",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalIndicator",
            fields=[
                ("id", models.IntegerField(blank=True, db_index=True)),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de eliminacion"
                    ),
                ),
                ("descount_value", models.PositiveSmallIntegerField(default=0)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "category_product",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="products.categoryproduct",
                        verbose_name="Indicador de descuento",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Indicador de Oferta",
                "verbose_name_plural": "historical Indicadores de oferta",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalCategoryProduct",
            fields=[
                ("id", models.IntegerField(blank=True, db_index=True)),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de eliminacion"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        db_index=True, max_length=50, verbose_name="Descripcion"
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Categoria de producto",
                "verbose_name_plural": "historical Categorias de productos",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
