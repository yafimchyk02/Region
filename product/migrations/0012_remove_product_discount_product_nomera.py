# Generated by Django 4.0 on 2022-06-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.AddField(
            model_name='product',
            name='nomera',
            field=models.TextField(default=None, max_length=500),
        ),
    ]
