from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class ProductExactCategory(models.Model):
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    name_exact = models.CharField(max_length=100, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return " %s" % self.name_exact

    class Meta:
        verbose_name = 'Подкатегория товара'
        verbose_name_plural = 'Подкатегории товаров'


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    articul = models.CharField(max_length=30, default=None)
    description = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=True)
    nomera = models.TextField(max_length=500, default=None)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    podcategory = models.ForeignKey(ProductExactCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    podcategory = models.ForeignKey(ProductExactCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default=None, blank=True, null=True)
    articul = models.CharField(max_length=150, default=None, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.product

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

# Create your models here.
