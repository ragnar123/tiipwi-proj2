from django.contrib.auth.models import User
from weather_station.models import SensorNode
import datetime
import string
import random

DEFAULT_SIZE=12

class securelayer:

    def pswGenerator(self, psw_size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(psw_size))

    def createNewUser(self, device_mac):
        user = User.objects.create_user(device_mac, email=None, password=None)
        password = self.pswGenerator(DEFAULT_SIZE)

        user.set_password(self.pswGenerator(DEFAULT_SIZE))
        #user.groups.add(authenticated_sensor_group)
        return [user, password];

    def checkPassword (self, raw_password):
        return check_password(raw_password)
