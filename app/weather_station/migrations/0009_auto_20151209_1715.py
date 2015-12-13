# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0008_auto_20151209_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensornode',
            name='first_seen',
            field=models.DateTimeField(default=None, null=True, verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
    ]
