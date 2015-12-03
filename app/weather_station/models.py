from django.db import models
import json

class SensorNode(models.Model):
    first_seen = models.DateTimeField('date published')
    sensor_id = models.IntegerField(default=0)
    position = models.CharField(max_length=200, default='POSITION NOT AVAILABLE.') # Prefer lat/lng coordinates

    def __str__(self):
        return "Sensor node #%s" % self.sensor_id



class SensorReading(models.Model):
    node = models.ForeignKey(SensorNode, default=-1)
    timestamp = models.DateTimeField('date published') # stamped at db insertion
    type = models.CharField(max_length=30, default='UNDEFINED')
    value = models.DecimalField(default=-1, max_digits=8, decimal_places=2)
