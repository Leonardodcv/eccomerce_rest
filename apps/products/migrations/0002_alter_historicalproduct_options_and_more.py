# Generated by Django 4.0.3 on 2023-02-10 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalproduct',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Modelo Base', 'verbose_name_plural': 'historical Modelos Base'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Modelo Base', 'verbose_name_plural': 'Modelos Base'},
        ),
        migrations.RemoveField(
            model_name='categoryproduct',
            name='measureunit',
        ),
        migrations.RemoveField(
            model_name='historicalcategoryproduct',
            name='measureunit',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='category_product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Categoria del producto'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='measure_unit',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Unidad de medida'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoria del producto'),
        ),
        migrations.AddField(
            model_name='product',
            name='measure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de medida'),
        ),
    ]
