# Generated by Django 4.0 on 2022-08-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_productimage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='articul',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
