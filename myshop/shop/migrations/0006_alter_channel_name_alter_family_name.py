# Generated by Django 4.1.3 on 2022-12-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_stock_alter_product_weight_gross'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]