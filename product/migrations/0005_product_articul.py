# Generated by Django 4.0 on 2022-06-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='articul',
            field=models.CharField(default=None, max_length=30),
        ),
    ]