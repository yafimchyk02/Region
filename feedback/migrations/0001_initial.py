# Generated by Django 4.0 on 2022-06-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Имя', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Телефон', models.CharField(default=None, max_length=16, unique=True)),
                ('Тема', models.CharField(max_length=30)),
                ('Сообщение', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Заявка клиента',
                'verbose_name_plural': 'Заявки клиентов',
            },
        ),
    ]
