# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 11:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0010_auto_20170917_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='milestone',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 11, 6, 6, 956806, tzinfo=utc)),
        ),
    ]
