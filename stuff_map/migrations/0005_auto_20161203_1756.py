# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff_map', '0004_auto_20161203_1755'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
        migrations.RenameModel(
            old_name='Locations',
            new_name='Location',
        ),
    ]
