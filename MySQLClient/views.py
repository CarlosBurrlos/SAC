
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("SQLDB client\n.")

def get(request, queryString):
    # Here we wil setup a 'GET' request
    # This is a general method and will pipe to different get methods




    return HttpResponse("InformationGot")

def set(request):
    return HttpResponse("Note:: SAC is note handling SET requests at the moment\n")


def verifyQueryString(queryString):

# Filter by store, Filter by audit ID, Grab variance specifications for a single Audit ID
# Then run just general SELECT, JOIN, ETC.
