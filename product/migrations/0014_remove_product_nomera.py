# Generated by Django 4.0 on 2022-06-22 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_nomera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='nomera',
        ),
    ]
