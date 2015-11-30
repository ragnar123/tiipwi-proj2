from django.shortcuts import render
from django.http import HttpResponse
from gmapi import maps
from gmapi.forms.widgets import GoogleMap

# Create your views here.


class get_populated_map(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))


def index(request):
    context = {'form': MapForm(initial={'map': map})}
    return HttpResponse("You're looking at the RPI weather station. <br>Try to go to /info/NODEID ",context)

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
