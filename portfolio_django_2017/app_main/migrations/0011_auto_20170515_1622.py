# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0010_auto_20170515_0732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examplespython',
            old_name='image',
            new_name='image_file',
        ),
    ]
