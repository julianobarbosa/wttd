# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170629_1949'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
    ]