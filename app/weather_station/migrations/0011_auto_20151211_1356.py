# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0010_auto_20151209_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensornode',
            name='sensor_id',
            field=models.CharField(unique=True, max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='humidity',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='lat',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='light',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='lon',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='pressure',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='wind_speed',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
