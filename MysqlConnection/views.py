import sqlvalidator
import re
import exceptions

from django.shortcuts import render
from django.http import HttpResponse
from .models import Snapshot, VarianceReport, EditcountsqtyVariance


# Create your views here.

def index(request):
    return HttpResponse("SQLDB client\n.")

# Note we are not going to need to verify our query string. Rather we will want to
# use a filter on the Model class
    # Look into setting up model handlers
    # Look into using .get() which can return an exception

def get(request, queryString):
    # Here we wil setup a 'GET' request
    # This is a general method and will pipe to different get methods
    try:
        cleanQueryString = verifyQueryString(queryString)
    except exceptions.MySQLClientError:
        # TODO :: Implement a standard logging mechanism
        pass

    # Now using the query string we have, send the query over
    # to the DB we have





    return HttpResponse("InformationGot")

def set(request):
    return HttpResponse("Note:: SAC is note handling SET requests at the moment\n")

# NOTE :: We may not need this since we aren't passing actual queries to API

def verifyQueryString(queryString):
    # Prune our string of hidden characters
    cleanedString = re.sub(r"[^a-zA-Z0-9]+", ' ', queryString)
    query = sqlvalidator.parse(cleanedString)
    if not query.is_valid():
        raise exceptions.MySQLClientError("Invalid User Query Request", exceptions.errors.MSQLCLIENTERR, queryString)
    return cleanedString

# Filter by store, Filter by audit ID, Grab variance specifications for a single Audit ID
# Then run just general SELECT, JOIN, ETC.
def Showemp(request):
    resultsdisplay = Snapshot.objects.all()
    return render(request, "BasicFormConnection.html", {"SnapReportForm": resultsdisplay})

def VarianceReportShower(request):
    resultsdisplay = VarianceReport.objects.filter(varianceqty__lt=-2).order_by('varianceqty')
    return render(request, "VarianceReport.html", {"VarianceReportForm": resultsdisplay})

def EditCountsReport(request):
    resultsdisplay = EditcountsqtyVariance.objects.all()
    return render(request, "edit_counts.html", {"EditCountsForm": resultsdisplay})