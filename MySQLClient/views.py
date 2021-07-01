from django.shortcuts import render
from django.http import HttpResponse
from .models import Snapshot, VarianceReport


# Create your views here.

def index(request):
    return HttpResponse("SQLDB client\n.")

def Showemp(request):
    resultsdisplay = Snapshot.objects.all()
    return render(request, "BasicFormConnection.html", {"SnapReportForm": resultsdisplay})

def VarianceReportShower(request):
    resultsdisplay = VarianceReport.objects.filter(varianceqty__lt=-2).order_by('varianceqty')
    return render(request, "VarianceReport.html", {"VarianceReportForm": resultsdisplay})
:q