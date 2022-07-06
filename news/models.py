from django.db import models


class News(models.Model):
    name = models.CharField(max_length=20, blank=False, default=None)
    text = models.TextField(max_length=300, blank=False, default=None)
    is_active = models.BooleanField(default=True)
    data = models.CharField(max_length=10, default=None)

    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# Create your models here.
