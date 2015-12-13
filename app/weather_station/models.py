""" Database models """
from django.db import models

class SensorNode(models.Model):
    """ Sensor Node """
    first_seen = models.DateTimeField('date published', default=None, blank=True, null=True)
    sensor_id = models.CharField(max_length=6, unique=True)

    # Prefer lat/lng coordinates
    position = models.CharField(max_length=200, default='POSITION NOT AVAILABLE.')

    def __str__(self):
        return "Sensor node #%s" % self.sensor_id

    def get_number_of_readings(self):
        """ Returns the number of readings attached to a sensor. """
        readings = SensorReading.objects.filter(node=self)
        self.num_readings = len(readings)
        return len(readings)

    num_readings = -1


class SensorReading(models.Model):
    """ Sensor Reading """

    node = models.ForeignKey(SensorNode, to_field='sensor_id')

    # stamped at db insertion *OR* timestamped at creation time.
    timestamp = models.DateTimeField('date published')
    light = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    temp = models.CharField(max_length=30, default='UNDEFINED', blank=True, null=True)
    humidity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pressure = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    wind_speed = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    lon = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    altitude = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sealevel_pressure = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
