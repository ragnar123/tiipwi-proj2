# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensornode',
            name='position',
            field=models.CharField(default=b'POSITION NOT AVAILABLE.', max_length=200),
            preserve_default=True,
        ),
    ]
