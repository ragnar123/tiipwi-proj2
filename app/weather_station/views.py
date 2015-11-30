from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("You're looking at the RPI weather station. <br>Try to go to /info/NODEID ")


def info(request, paramtere):
    return HttpResponse("NODE ID: %s.\n\n To serve: { temp: n, humid: n, .... to be defined }" % paramtere )
