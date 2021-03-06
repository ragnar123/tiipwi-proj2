""" Django Views """
import datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import JsonResponse
from django.db import transaction
from django.contrib.auth.models import User

from weather_station.models import SensorNode
from weather_station.models import SensorReading
from weather_station.securelayer import securelayer
from weather_station.authentication import Authentication

def sort_by_num_readings(x, y):
    return x.num_readings - y.num_readings;

REFRESH_RATE = 10
# Main page. Shows map & list of nodes
def index(request):
    """ The main page """
    template = loader.get_template('index.html')

    nodes = SensorNode.objects.all()
    for node in nodes:
        node.get_number_of_readings()

    # TODO: Sort nodes by readings.
    # node.num_readings
    nodes = sorted(nodes, cmp=sort_by_num_readings, reverse=True)

    context = RequestContext(request, {
        'sensor_list': nodes,
    })
    return HttpResponse(template.render(context))

def get_sensor_readings(node_id):
    """ util function """
    readings = SensorReading.objects.filter(node_id=node_id)
    out = []
    for reading in readings:
        out.append({
            'timestamp': reading.timestamp,
            'temp': reading.temp,
            'pressure': reading.pressure,
            'humidity': reading.humidity,
            'light': reading.light,
            'wind_speed': reading.wind_speed,
            'lat': reading.lat,
            'lon': reading.lon,
            'altitude': reading.altitude,
            'sealevel_pressure': reading.sealevel_pressure
        })
    return out


# Information about a single node
def info(request, node_id):
    response_data = {}
    response_data['sensor_id'] = node_id

    # If the node_id is purely numberical, we might do the SensorNode
    # else we might have to fetch a user
    resp = SensorNode.objects.filter(sensor_id=node_id)
    if len(resp) == 1:
        node = resp[0]

        response_data['timestamp'] = node.first_seen
        response_data['position'] = node.position
        response_data['readings'] = get_sensor_readings(node)


    return JsonResponse(response_data)

def node_list(request):
    """ Returns a array of nodes. """
    response_data = []

    nodes = SensorNode.objects.all()
    for node in nodes:
        node.get_number_of_readings()
        node_data = {}
        node_data['sensor_id'] = node.sensor_id
        node_data['position'] = node.position
        node_data['num_readings'] = node.num_readings;
        if node.num_readings > 0:
            response_data.append(node_data)

        # We need to extract: nodeis, position, last readings, etc?
        # 1. fetch the sensor readings from db.

    return JsonResponse(response_data, safe=False)


# View to show graphs of the recieved data for a node
def plots(request, node_id):
    """ used for the /plots/sensorID route """
    template = loader.get_template('plots.html')
    nodes = SensorNode.objects.get(sensor_id=node_id)

    sensors = []
    readings = SensorReading.objects.filter(node_id=nodes.id)


    context = RequestContext(request, {
        'sensors': sensors,
        'sensor_id': node_id,
        'readings': get_sensor_readings(node_id)
    })
    return HttpResponse(template.render(context))



def ifAuthenticatedAddEntry(user_id, raw_password):
    try:
        node = SensorNode.objects.get(sensor_id=user_id)
    except SensorNode.DoesNotExist:
        return HttpResponse("Unable to find node")
    except SensorNode.MultipleObjectsReturned:
        return HttpResponse("Should never occur!")

    if securelayer.checkPassword(raw_password):
        new_entry = SensorReading(node_id=user_id, timestamp=str(datetime.datetime.now()))
        new_entry.save()
    else:
        return "sorry wrong password"




@transaction.atomic
def signup(request):
    """The idea is that this will return a new nodeid & key."""
    s = securelayer()
    # The master controller will create a new, unique name for connecting nodes.
    # If, and only if, the nodes have not connected before.

    # The client node is responsible for *saving* the received node_id
    # to persistent memory!!!
    # -> resource directory
    name = s.pswGenerator(6)
    # check if the newly, randomly generated name is UNIQUE! regenerate, if not.
    [user, password] = s.createNewUser(name)

    response_data = {}
    response_data['username'] = name
    response_data['password'] = password

    # Also, create a sensorNode with username!
    sensor_node = SensorNode(sensor_id=name)
    sensor_node.save()

    # I should test the new user (by running user.check_password)
    # to see if valid (guessing it always is...)

    print "INFO for check:" + name + "," + password
    u = User.objects.get(username=name)

    return JsonResponse(response_data)



auth = Authentication()


#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def put_reading(request, node_id):
    # Valid values for type: { light,   temperature, humidity, wind_speed, atmospheric_pressure }
    # Valid units:           { cd/m^2,  C,           %,        m/s,        hPa / bar            }

    try:
        username = request.POST.get('username')
        password = request.POST.get('password')

        SensorNode.objects.get(sensor_id=node_id)
        authenticated = auth.ifAuthenticatedAddEntry(username, password)

    except SensorNode.DoesNotExist:
        return JsonResponse({"message": "Unable to find node"})

    if authenticated is True:
        light = request.POST.get('light')
        temp = request.POST.get('temp')
        pressure = request.POST.get('pressure')
        humidity = request.POST.get('humidity')
        wind_speed = request.POST.get('wind_speed')
        time = request.POST.get('time')
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        altitude = request.POST.get('altitude')
        sealevel_pressure = request.POST.get('sealevel_pressure')

        reading = SensorReading(
            # node=node,
            node_id=request.POST.get('username'),
            timestamp=time, #str(datetime.datetime.now()), # Should *maybe* be time
            # it at least changes some assumptions on the data.
            temp=temp,
            pressure=pressure,
            humidity=humidity,
            wind_speed=wind_speed,
            lat=lat,
            lon=lon,
            light=light,
            altitude=altitude,
            sealevel_pressure=sealevel_pressure
        )

        print request.POST.get('username', 'NOT_AUTHENTICATED')

        reading.save()
        response_data = {}
        response_data['refresh_interval'] = REFRESH_RATE
        return JsonResponse(response_data)
    else:
        return JsonResponse({"message": "Login error. Provide valid username & password!."})
