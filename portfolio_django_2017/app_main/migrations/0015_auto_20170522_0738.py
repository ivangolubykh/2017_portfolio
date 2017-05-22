# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0014_auto_20170522_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveSmallIntegerField(db_index=True, help_text='Порядковый номер объекта на странице', unique=True, verbose_name='Порядковый номер объекта на странице')),
                ('text', models.TextField(help_text='Описание места работы', verbose_name='Описание места работы')),
            ],
        ),
        migrations.RemoveField(
            model_name='worksheaderorlist2text',
            name='up',
        ),
        migrations.RemoveField(
            model_name='worksheaderorlist3text',
            name='up',
        ),
        migrations.RemoveField(
            model_name='worksheaderorlist4text',
            name='up',
        ),
        migrations.RemoveField(
            model_name='workstext',
            name='up',
        ),
        migrations.DeleteModel(
            name='WorksHeaderorList1Text',
        ),
        migrations.DeleteModel(
            name='WorksHeaderorList2Text',
        ),
        migrations.DeleteModel(
            name='WorksHeaderorList3Text',
        ),
        migrations.DeleteModel(
            name='WorksHeaderorList4Text',
        ),
        migrations.DeleteModel(
            name='WorksText',
        ),
    ]