from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("You're looking at the RPI weather station. <br>Try to go to /info/NODEID ")

def info(request, paramtere):
    return HttpResponse("NODE ID: %s.\n\n To serve: { temp: n, humid: n, .... to be defined }" % paramtere )


def list(request):
    from weather_station.models import SensorNode
    nodes = SensorNode.objects.all()
    resp = "LIST OF CONNECTED NODES / all " + str(nodes)
    return HttpResponse(resp)

def signup(request):
    resp = "The idea is that this will return a new nodeid & key."
    return HttpResponse(resp)

