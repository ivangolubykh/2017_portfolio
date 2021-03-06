# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0011_auto_20170515_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamplesJs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveSmallIntegerField(db_index=True, help_text='Порядковый номер объекта на странице', unique=True, verbose_name='Порядковый номер объекта на странице')),
                ('name_project', models.CharField(help_text='Название проекта', max_length=255, verbose_name='Название проекта')),
                ('image_file', models.ImageField(blank=True, upload_to='examples_js_images/', verbose_name='Картинка проекта')),
                ('net_address', models.CharField(blank=True, help_text='Ссылка на проект в сети', max_length=255, verbose_name='Ссылка на проект в сети')),
                ('git_address', models.CharField(blank=True, help_text='Ссылка на git-репозиторий проекта', max_length=255, verbose_name='Ссылка на git-репозиторий проекта')),
                ('text', models.TextField(help_text='Описание проекта', verbose_name='Описание проекта')),
            ],
        ),
        migrations.RemoveField(
            model_name='examplesjsheaderorlist2text',
            name='up',
        ),
        migrations.RemoveField(
            model_name='examplesjsheaderorlist3text',
            name='up',
        ),
        migrations.RemoveField(
            model_name='examplesjsheaderorlist4text',
            name='up',
        ),
        migrations.RemoveField(
            model_name='examplesjstext',
            name='up',
        ),
        migrations.DeleteModel(
            name='ExamplesJsHeaderorList1Text',
        ),
        migrations.DeleteModel(
            name='ExamplesJsHeaderorList2Text',
        ),
        migrations.DeleteModel(
            name='ExamplesJsHeaderorList3Text',
        ),
        migrations.DeleteModel(
            name='ExamplesJsHeaderorList4Text',
        ),
        migrations.DeleteModel(
            name='ExamplesJsText',
        ),
    ]
