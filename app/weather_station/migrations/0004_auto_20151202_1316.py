# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0003_sensorreading_node'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorreading',
            name='type',
            field=models.CharField(default=b'UNDEFINED', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sensorreading',
            name='value',
            field=models.DecimalField(default=-1, max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
