# Generated by Django 4.0 on 2022-06-22 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_productimage_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
