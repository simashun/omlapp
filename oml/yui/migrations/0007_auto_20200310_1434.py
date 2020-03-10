# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-10 05:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yui', '0006_auto_20200310_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_oml3',
            name='Del_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='削除年月日'),
        ),
        migrations.AlterField(
            model_name='t_oml3',
            name='Up_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 5, 34, 53, 893735, tzinfo=utc), null=True, verbose_name='更新年月日'),
        ),
    ]
