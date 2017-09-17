# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 10:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0007_auto_20170917_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='milestone',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 10, 47, 32, 594016, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.Profile'),
        ),
    ]
