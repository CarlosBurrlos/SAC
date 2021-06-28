from django.shortcuts import render
from django.http import HttpResponse
from .models import Snapshot


# Create your views here.

def index(request):
    return HttpResponse("SQLDB client\n.")

def Showemp(request):
    resultsdisplay = Snapshot.objects.all()
    return render(request, "BasicFormConnection.html", {"SnapReportForm": resultsdisplay})
