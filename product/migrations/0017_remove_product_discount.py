# Generated by Django 4.0 on 2022-06-22 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_remove_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
    ]
