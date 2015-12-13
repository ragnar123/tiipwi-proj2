# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0011_auto_20151211_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorreading',
            name='altitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sensorreading',
            name='sealevel_pressure',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
