# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0002_weather_for_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamplesPythonHeaderorList1Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveSmallIntegerField(db_index=True, help_text='Порядковый номер заголовка h1 на странице', unique=True, verbose_name='Порядковый номер заголовка h1 на странице')),
                ('text', models.CharField(blank=True, help_text='Заголовки (h1) для страницы примеров работ', max_length=255, verbose_name='Заголовки (h1) для страницы примеров работ')),
            ],
        ),
        migrations.CreateModel(
            name='ExamplesPythonHeaderorList2Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveSmallIntegerField(db_index=True, help_text='Порядковый номер заголовка h2 на странице', unique=True, verbose_name='Порядковый номер заголовка h2 на странице')),
                ('text', models.CharField(blank=True, help_text='Заголовки (h2) для главной страницы', max_length=255, verbose_name='Заголовки (h2) для главной страницы')),
                ('up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.ExamplesPythonHeaderorList1Text')),
            ],
        ),
        migrations.CreateModel(
            name='ExamplesPythonHeaderorList3Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveSmallIntegerField(db_index=True, help_text='Порядковый номер заголовка h3 на странице', unique=True, verbose_name='Порядковый номер заголовка h3 на странице')),
                ('text', models.CharField(blank=True, help_text='Заголовки (h3) для главной страницы', max_length=255, verbose_name='Заголовки (h3) для главной страницы')),
                ('up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.ExamplesPythonHeaderorList2Text')),
            ],
        ),
        migrations.CreateModel(
            name='ExamplesPythonHeaderorList4Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveSmallIntegerField(db_index=True, help_text='Порядковый номер заголовка h4 на странице', unique=True, verbose_name='Порядковый номер заголовка h4 на странице')),
                ('text', models.CharField(blank=True, help_text='Заголовки (h4) для главной страницы', max_length=255, verbose_name='Заголовки (h4) для главной страницы')),
                ('up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.ExamplesPythonHeaderorList3Text')),
            ],
        ),
        migrations.CreateModel(
            name='ExamplesPythonText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveSmallIntegerField(db_index=True, help_text='Порядковый номер абзаца в тексте', unique=True, verbose_name='Порядковый номер абзаца в тексте')),
                ('text', models.TextField(help_text='Текст абзаца', verbose_name='Текст абзаца')),
                ('up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.ExamplesPythonHeaderorList4Text')),
            ],
        ),
    ]
