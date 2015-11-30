from django.db import models

# Create your models here.

class SensorReading(models.Model):
    timestamp = models.DateTimeField('date published') # stamped at db insertion

class SensorNode(models.Model):
    first_seen = models.DateTimeField('date published')
    sensor_id = models.IntegerField(default=0)
    position = models.CharField(max_length=200,default='POSITION NOT AVAILABLE.') # Prefer lat/lng coordinates


