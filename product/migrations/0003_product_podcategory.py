# Generated by Django 4.0 on 2022-06-08 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productcategory_options_productexactcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='podcategory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productexactcategory'),
        ),
    ]
