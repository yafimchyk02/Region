# Generated by Django 4.0 on 2022-08-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_product_is_metiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_metiz',
            field=models.BooleanField(default=True),
        ),
    ]
