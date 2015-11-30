from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


from weather_station.models import SensorNode



def index(request):
    template = loader.get_template('index.html')

    nodes = SensorNode.objects.all()
    context = RequestContext(request, {
        'sensor_list': nodes,
    })
    return HttpResponse(template.render(context))

def info(request, paramtere):
    return HttpResponse("NODE ID: %s.\n\n To serve: { temp: n, humid: n, .... to be defined }" % paramtere )


def list(request):
    nodes = SensorNode.objects.all()
    resp = "LIST OF CONNECTED NODES / all " + str(nodes)
    return HttpResponse(resp)

def signup(request):
    resp = "The idea is that this will return a new nodeid & key."
    return HttpResponse(resp)
