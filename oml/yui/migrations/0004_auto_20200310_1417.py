# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-10 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yui', '0003_auto_20200310_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_oml3',
            name='Hachu_no2',
        ),
        migrations.AlterField(
            model_name='t_oml3',
            name='Biken_flg',
            field=models.IntegerField(default='0', verbose_name='美健フラグ'),
        ),
        migrations.AlterField(
            model_name='t_oml3',
            name='Cancel_flg',
            field=models.IntegerField(default='0', verbose_name='キャンセルフラグ'),
        ),
        migrations.AlterField(
            model_name='t_oml3',
            name='Open_flg',
            field=models.IntegerField(default='0', verbose_name='公開フラグ'),
        ),
    ]