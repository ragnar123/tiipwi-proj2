# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0005_auto_20151208_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorreading',
            name='lat',
            field=models.DecimalField(default=-1, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sensorreading',
            name='light',
            field=models.DecimalField(default=-1, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sensorreading',
            name='lon',
            field=models.DecimalField(default=-1, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sensorreading',
            name='wind_speed',
            field=models.DecimalField(default=-1, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
    ]
