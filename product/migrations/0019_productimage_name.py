# Generated by Django 4.0 on 2022-08-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_nomera'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]