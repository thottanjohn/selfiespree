# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_auto_20170719_2348'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
    ]