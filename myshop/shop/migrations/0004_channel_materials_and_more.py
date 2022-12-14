# Generated by Django 4.1.3 on 2022-12-02 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_family_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='E-Commerce', max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'channel',
                'verbose_name_plural': 'channels',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['label'],
            },
        ),
        migrations.AddIndex(
            model_name='materials',
            index=models.Index(fields=['label'], name='shop_materi_label_dd1bea_idx'),
        ),
        migrations.AddIndex(
            model_name='channel',
            index=models.Index(fields=['name'], name='shop_channe_name_b94857_idx'),
        ),
        migrations.AddField(
            model_name='product',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_channel', to='shop.channel'),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_products', to='shop.materials'),
        ),
    ]
