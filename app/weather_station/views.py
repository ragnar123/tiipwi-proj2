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
    response_data['id'] = node_id
    response_data['position'] = [56.1572, 10.2107]

    resp = SensorNode.objects.filter(sensor_id=node_id)
    if len(resp) == 1:
        response_data['timestamp'] = resp[0].first_seen

    return JsonResponse(response_data)

def list(request):
    response_data = []

    nodes = SensorNode.objects.all()
    for node in nodes:
        node_data = {}
        node_data['id'] = node.sensor_id
        node_data['position'] = [56.1572, 10.2107]
        response_data.append(node_data)

        # We need to extract: nodeis, position, last readings, etc?
        # 1. fetch the sensor readings from db.

    return JsonResponse(response_data, safe=False)

def signup(request):
    resp = "The idea is that this will return a new nodeid & key."
    return HttpResponse(resp)
