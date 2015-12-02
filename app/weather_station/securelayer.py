from django.contrib.auth.models import User
from weather_station.models import SensorNode
import datetime
import string
import random

DEFAULT_SIZE=6

class securelayer:

    def pswGenerator(psw_size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(psw_size))

    def createNewUser(device_mac):
        user = User.objects.create_user(device_mac, email=None, password=None)
        password = pswGenerator(DEFAULT_SIZE)

        user.set_password(pswGenerator(DEFAULT_SIZE))
        #user.groups.add(authenticated_sensor_group)
        return [user, password];

    def checkPassword (raw_password):
        return check_password(raw_password)
