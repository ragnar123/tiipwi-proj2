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
        user.save()


    def ifAuthenticatedAddEntry(self, user_id, raw_password):
        # Distinction between User and SensorNode. ? (/signup produces a username.)
        # Sensor_ID is now 6digit string (was 4 digit numeric) (migration ok)
        print user_id
        try:
            user = User.objects.get(username=user_id)
            print ("CHECKING USER " + user_id + ". IF PW " + raw_password + " is valid..");
            if user.check_password(raw_password):
                print "We were able to authenticate you."
                print "need to initialize a SensorNode with id as yours"
                sn = SensorNode.objects.get(sensor_id = user_id)
                if not sn:
                    print "not found. creating"
                    sn = SensorNode(sensor_id = user_id)
                    sn.save();

                return True

            else:
                raise Exception('User not known.')
        except SensorNode.DoesNotExist:
            print "fail"
        except Exception as failure:
            print "wrong PW" + str(failure)
            return False;
