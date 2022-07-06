from django.db import models


class Peoples(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None, name="Имя")
    tel = models.CharField(blank=False, max_length=16, default=None, name="Телефон")
    topic = models.CharField(max_length=30, name="Тема")
    text = models.TextField(max_length=500, name="Сообщение")

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Заявка клиента'
        verbose_name_plural = 'Заявки клиентов'
# Create your models here.
