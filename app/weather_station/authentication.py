from django.contrib.auth.models import User
from weather_station.models import SensorNode
import datetime
import string
import random

DEFAULT_SIZE=6

class Authentication:
    def psw_generator(psw_size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(psw_size))

    def createNewUser(device_mac):
        user = User.objects.create_user(device_mac, mail=None, password=None)
        user.set_password(psw_generator(DEFAULT_SIZE))
        user.groups.add(authenticated_sensor_group)


    def ifAuthenticatedAddEntry(self, user_id, raw_password):
        # Distinction between User and SensorNode. ? (/signup produces a username.)
        # Sensor_ID is now 6digit string (was 4 digit numeric) (migration ok)
        try:
            node = SensorNode.objects.get(sensor_id=user_id)
        except SensorNode.DoesNotExist:
            # Throw exception
            print "fail"

        user = User(username=user_id)
        if user.check_password(raw_password):
            new_entry = SensorReading(node_id=user_id , timestamp= str(datetime.datetime.now()))
            new_entry.save()
        else:
            return "sorry wrong password"
