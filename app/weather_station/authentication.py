from django.contrib.auth.models import User
from weather_station.models import SensorNode
import datetime
import string
import random

global DEFAULT_SIZE=6

def psw_generator(psw_size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(psw_size))

def createNewUser(device_mac):
    user = User.objects.create_user(device_mace, mail=None, password=None)
    user.set_password(psw_generator(DEFAULT_SIZE))
    user.groups.add(authenticated_sensor_group)


def ifAuthenticatedAddEntry(user_id, raw_password)
    try:
        node = SensorNode.objects.get(sensor_id=user_id)
    except SensorNode.DoesNotExist:
        return HttpResponse("Unable to find node");
    except SensorNode.MultipleObjectsReturned:
        return HttpResponse("her er heilt galid!");

    if check_password(raw_password):
        new_entry = SensorReading(node_id=user_id , timestamp= str(datetime.datetime.now())
        new_entry.save()
    else:
        return "sorry wrong password"
