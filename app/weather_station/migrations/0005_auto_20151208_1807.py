# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0004_auto_20151202_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensorreading',
            name='type',
        ),
        migrations.RemoveField(
            model_name='sensorreading',
            name='value',
        ),
        migrations.AddField(
            model_name='sensorreading',
            name='humidity',
            field=models.DecimalField(default=-1, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sensorreading',
            name='pressure',
            field=models.DecimalField(default=-1, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sensorreading',
            name='temp',
            field=models.CharField(default=b'UNDEFINED', max_length=30),
            preserve_default=True,
        ),
    ]
