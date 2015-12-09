from django.db import models
import json

class SensorNode(models.Model):
    first_seen = models.DateTimeField('date published')
    sensor_id = models.CharField(max_length=6,default='STUPID')
    position = models.CharField(max_length=200, default='POSITION NOT AVAILABLE.') # Prefer lat/lng coordinates

    def __str__(self):
        return "Sensor node #%s" % self.sensor_id

    def getNumberOfReadings(self):
        readings = SensorReading.objects.filter(node=self)
        return len(readings)



class SensorReading(models.Model):
    node = models.ForeignKey(SensorNode, default=-1)
    timestamp = models.DateTimeField('date published') # stamped at db insertion *OR* timestamped at creation time.
    light = models.DecimalField(default=-1, max_digits=8,decimal_places=2, blank=True, null=True) # I have *NO* idea what reasonable defaults are. please fix/improve
    temp = models.CharField(max_length=30, default='UNDEFINED',blank=True, null=True)
    humidity = models.DecimalField(default=-1, max_digits=8, decimal_places=2, blank=True, null=True)
    pressure = models.DecimalField(default=-1, max_digits=8, decimal_places=2, blank=True, null=True)
    wind_speed = models.DecimalField(default=-1, max_digits=8, decimal_places=2, blank=True, null=True)
    lat = models.DecimalField(default=-1, max_digits=8, decimal_places=2, blank=True, null=True)
    lon = models.DecimalField(default=-1, max_digits=8, decimal_places=2, blank=True, null=True)
