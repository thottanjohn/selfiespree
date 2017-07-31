# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 09:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0011_auto_20170722_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='userlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite', models.BooleanField(default='False')),
            ],
        ),
        migrations.RemoveField(
            model_name='picture',
            name='favourite',
        ),
        migrations.AddField(
            model_name='picture',
            name='image_id',
            field=models.BigIntegerField(default=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlike',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Picture'),
        ),
        migrations.AddField(
            model_name='userlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]