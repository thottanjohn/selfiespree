# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfiecontest', '0010_auto_20170724_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlike',
            name='like_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userlike',
            name='image_id',
            field=models.IntegerField(),
        ),
    ]
