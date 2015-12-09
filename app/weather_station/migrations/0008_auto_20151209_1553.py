# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station', '0007_auto_20151208_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorreading',
            name='humidity',
            field=models.DecimalField(default=-1, null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='lat',
            field=models.DecimalField(default=-1, null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='light',
            field=models.DecimalField(default=-1, null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='lon',
            field=models.DecimalField(default=-1, null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='pressure',
            field=models.DecimalField(default=-1, null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='temp',
            field=models.CharField(default=b'UNDEFINED', max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensorreading',
            name='wind_speed',
            field=models.DecimalField(default=-1, null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
