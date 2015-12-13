# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0009_auto_20151209_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensornode',
            name='sensor_id',
            field=models.CharField(default=b'STUPID', unique=True, max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='node',
            field=models.ForeignKey(to='weather_station.SensorNode', to_field=b'sensor_id'),
            preserve_default=True,
        ),
    ]
