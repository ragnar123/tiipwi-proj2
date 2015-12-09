# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0006_auto_20151208_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensornode',
            name='sensor_id',
            field=models.CharField(default=b'STUPID', max_length=6),
            preserve_default=True,
        ),
    ]
