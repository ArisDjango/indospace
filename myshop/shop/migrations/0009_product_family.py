# Generated by Django 4.1.3 on 2022-12-03 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_product_channel_product_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_family', to='shop.family'),
        ),
    ]
