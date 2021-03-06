# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather_For_Json',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True, help_text='Дата и время последнего сохранения данных погоды из api', verbose_name='Дата и время последнего сохранения данных погоды из api')),
                ('image', models.CharField(blank=True, help_text='Путь к файлу картинки погоды', max_length=255, verbose_name='Путь к файлу картинки погоды')),
                ('temperature', models.CharField(blank=True, help_text='Температура воздуха', max_length=10, verbose_name='Температура воздуха')),
                ('text', models.CharField(blank=True, help_text='Текстовое описание погоды, например: Солнечно', max_length=100, verbose_name='Текстовое описание погоды, например: Солнечно')),
            ],
        ),
    ]
