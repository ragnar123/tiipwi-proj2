# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0002_sensornode_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorreading',
            name='node',
            field=models.ForeignKey(default=-1, to='weather_station.SensorNode'),
            preserve_default=True,
        ),
    ]
