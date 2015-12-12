import datetime
import string
import random

from django.contrib.auth.models import User
from weather_station.models import SensorNode

DEFAULT_SIZE = 12

class securelayer:
    """ Provides function related to user creation. """
    def pswGenerator(self, psw_size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(psw_size))

    def createNewUser(self, device_mac):
        user = User.objects.create_user(device_mac, email=None, password=None)
        password = self.pswGenerator(DEFAULT_SIZE)
        user.set_password(password)
        user.save()
        #user.groups.add(authenticated_sensor_group)
        return [user, password];
