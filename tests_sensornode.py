from django.test import TestCase
from weather_station.models import SensorNode

class SensorNodeTestCase(TestCase):
    def setUp(self):
        SensorNode.objects.create(sensor_id='abcdef', first_seen="2015-06-06")

    def test_verify_sensor_node(self):
        """Checking that the sensor readings are empty for new SensorNode"""
        sn1 = SensorNode.objects.get(sensor_id="abcdef")
        self.assertEqual(sn1.get_number_of_readings(), 0)

        self.assertEqual(sn1.sensor_id, 'abcdef')

