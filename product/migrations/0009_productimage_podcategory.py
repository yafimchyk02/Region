# Generated by Django 4.0 on 2022-06-08 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_productimage_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='podcategory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productexactcategory'),
        ),
    ]