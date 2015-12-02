from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import JsonResponse
from django.db import transaction

from weather_station.securelayer import securelayer


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



def ifAuthenticatedAddEntry(user_id, raw_password):
    try:
        node = SensorNode.objects.get(sensor_id=user_id)
    except SensorNode.DoesNotExist:
        return HttpResponse("Unable to find node");
    except SensorNode.MultipleObjectsReturned:
        return HttpResponse("her er heilt galid!");

    if securelayer.checkPassword(raw_password):
        new_entry = SensorReading(node_id=user_id , timestamp= str(datetime.datetime.now()))
        new_entry.save()
    else:
        return "sorry wrong password"




@transaction.atomic
def signup(request):
    resp = "The idea is that this will return a new nodeid & key."
    s = securelayer()
    # The master controller will create a new, unique name for connecting nodes.
    # If, and only if, the nodes have not connected before.

    # The client node is responsible for *saving* the received node_id
    # to persistent memory!!!
    # -> resource directory
    name = s.pswGenerator(12)
    # check if the newly, randomly generated name is UNIQUE! regenerate, if not.
    [user, password] = s.createNewUser(name)

    response_data = {}
    response_data['username'] = name
    response_data['password'] = password

    return JsonResponse(response_data);



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
