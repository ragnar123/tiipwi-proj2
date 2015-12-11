"""


"""
import requests
import os

from django.test import TestCase
from weather_station.models import SensorNode




class SensorNodeTestCase(TestCase):
    def setUp(self):
        SensorNode.objects.create(sensor_id='abcdef', first_seen="2015-06-06")

    def test_verify_signup(self):
        """
        this test case 
        sends a request to the live server
        and gets a username/password pair.
        """
        
        # Please do note that we are actually targeting production in our tests.
        # Not the local server... I should probably rewrite this.
        r = requests.get(os.environ.get("PRODUCTION_TUNNEL") + '/signup/')
        keypair = r.json()

        print keypair
        self.assertEqual(len(keypair['username']), 6)
        self.assertEqual(len(keypair['password']), 12)

        """
            TODO: do a cleanup afterwards.
        """










