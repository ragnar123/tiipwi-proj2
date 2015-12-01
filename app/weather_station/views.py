from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import JsonResponse

from weather_station.models import SensorNode
import json


# Main page. Shows map & list of nodes
def index(request):
    template = loader.get_template('index.html')

    nodes = SensorNode.objects.all()
    context = RequestContext(request, {
        'sensor_list': nodes,
    })
    return HttpResponse(template.render(context))

# Information about a single node
def info(request, node_id):
    response_data = {}
    response_data['sensor_id'] = node_id

    resp = SensorNode.objects.filter(sensor_id=node_id)
    if len(resp) == 1:
        node = resp[0]
        response_data['timestamp'] = node.first_seen
        response_data['position'] = node.position


    return JsonResponse(response_data)

def list(request):
    response_data = []

    nodes = SensorNode.objects.all()
    for node in nodes:
        node_data = {}
        node_data['sensor_id'] = node.sensor_id
        node_data['position'] = node.position
        response_data.append(node_data)

        # We need to extract: nodeis, position, last readings, etc?
        # 1. fetch the sensor readings from db.

    return JsonResponse(response_data, safe=False)



from django.contrib.auth.models import User
from weather_station.models import SensorNode
import datetime
import string
import random

DEFAULT_SIZE=6

def psw_generator(psw_size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(psw_size))

def createNewUser(device_mac):
    user = User.objects.create_user(device_mac, email=None, password=None)
    user.set_password(psw_generator(DEFAULT_SIZE))
    #user.groups.add(authenticated_sensor_group)


def ifAuthenticatedAddEntry(user_id, raw_password):
    try:
        node = SensorNode.objects.get(sensor_id=user_id)
    except SensorNode.DoesNotExist:
        return HttpResponse("Unable to find node");
    except SensorNode.MultipleObjectsReturned:
        return HttpResponse("her er heilt galid!");

    if check_password(raw_password):
        new_entry = SensorReading(node_id=user_id , timestamp= str(datetime.datetime.now()))
        new_entry.save()
    else:
        return "sorry wrong password"





def signup(request):
    resp = "The idea is that this will return a new nodeid & key."

    name = "asdf_unique+1"
    createNewUser(name)

    return HttpResponse(resp)



def put_reading(request, node_id, type, value):
    # :- if authenticated, proceed.
    # else, throw a 401!

    # Valid values for type: { temperature, humidity, wind_speed, atmospheric_pressure }
    # Valid units:           { C,          %,        m/s,        hPa / bar            }
    # From this, I think I am going to create some subclasses.
    try:
        node = SensorNode.objects.get(sensor_id=node_id)
    except SensorNode.DoesNotExist:
        return HttpResponse("Unable to find node");
    except SensorNode.MultipleObjectsReturned:
        return HttpResponse("her er heilt galid!");



    if type == "temperature":
        return HttpResponse("Saved your temps!");

    if type == "humidity":
        return HttpResponse("Saved your values");

    if type == "wind_speed":
        return HttpResponse("Saved your wind speeds!");

    if type == "atmospheric_pressure":
        return HttpResponse("Saved your values");


    return HttpResponse("I do not know what to do with your " + type);
