# Generated by Django 4.0 on 2022-06-08 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_productimage_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='podcategory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productexactcategory'),
        ),
    ]