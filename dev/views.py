from django.shortcuts import render
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import UploadFile, Snapshot, VarianceReport, EditcountsqtyVariance, Editcountbysku
from .forms import uploadFileForm, UpdateItem
from . import forms
from django.urls import reverse
from django.db.models import Q

# Create your views here.

def SAC(request:HttpRequest):
    # This will allow us to test field checking
    if request.method == 'POST':
        try:
            flag = request.POST['flag']
        except KeyError:
            index = reverse('/dev/')
            return HttpResponseRedirect(index)
        # TODO :: If we are able to test for a flag then we can perform a certain
        #         action based on the flags value
        #         e.g.) 0 >> run the read from scanner application
        if flag == 0:
            # Read from scanner
            response = render(request, 'report.html')
        elif flag == 1:
            # Read from RGIS/WIS
            response = render(request, 'index.html')
        else:
            response = render(request, 'report.html')
        return response
    response = render(request, 'index.html')
    return response

def EDITCOUNTS(request:HttpRequest):
    response = render(request, 'edit_counts.html')
    return response

def EXPORTAUDIT(request:HttpRequest):
    response = render(request, 'export_audit.html')
    return response

def REPORT(request:HttpRequest):
    response = render(request, 'report.html')
    return response

def index(request:HttpRequest):
    #response = render(request, 'DevIndex.html')
    return HttpResponse('Dev index page')

# View that presents client with

def testView(request:HttpRequest):
    response = render(request, 'DevTesting.html')
    return response

def handleFileUpload(file:UploadedFile):
    with open(
        "temp.txt",
        'wb+'
    ) as dest:
        for chunk in file.chunks():
            dest.write(chunk)

# TODO :: Setup some sort of fall back to handle this information
def upload(request:HttpRequest):
    if request.method =='POST':
        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handleFileUpload(request.FILES['upload'])
            redirect = reverse('uploadSuccess')
            return HttpResponseRedirect(redirect)
        else:
            return HttpResponse('Failed')
    else:
        form = uploadFileForm()
        return render(request, 'uploadFile.html', {'form': form})

def uploadSuccess(request:HttpRequest):
    return HttpResponse('File Successfully uploaded')

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

#view to get edit counts table results
def EditCountsReport(request):
    resultsdisplay = Editcountbysku.objects.all()
    auditID = request.GET.get('AuditID')
    greaterthen = request.GET.get('VarianceGreater')
    description = request.GET.get('Description')
    accepted = request.GET.get('Accepted')

#deleting session variables if new request
    if "description" in request.session and description == "":
        del request.session['description']
    if "greaterthen" in request.session and greaterthen == "":
        del request.session['greaterthen']
##    if "accepted" in request.session and accepted == "":
##        del request.session['accepted']

#applying search if identified variables exist in get command
    # if not check to see if session variables exist and apply those instead.
    # Repeat for all three variable types.
    if auditID != "" and auditID is not None:
        resultsdisplay = resultsdisplay.filter(auditid=auditID)
        request.session["auditID"] = auditID
    elif "auditID" in request.session:
        resultsdisplay = resultsdisplay.filter(auditid=request.session["auditID"])

    if description != "" and description is not None:
        resultsdisplay = resultsdisplay.filter(description__icontains=description)
        request.session["description"] = description
    elif "description" in request.session:
        resultsdisplay = resultsdisplay.filter(description__icontains=request.session["description"])

    if greaterthen != "" and greaterthen is not None:
        greaterthen = int(greaterthen)
        lessthen = int(greaterthen) * -1
        resultsdisplay = resultsdisplay.filter(Q(currentvariance__lt=lessthen) | Q(currentvariance__gt=greaterthen))
        request.session["greaterthen"] = greaterthen
    elif "greaterthen" in request.session:
        lessthen = int(request.session["greaterthen"]) * -1
        resultsdisplay = resultsdisplay.filter(Q(currentvariance__lt=lessthen) | Q(currentvariance__gt=request.session["greaterthen"]))

##    if accepted != "" and accepted is not None:
##        if accepted == "on":
##            accepted = "True"
##            resultsdisplay = resultsdisplay.filter(accepted=accepted)

    elif accepted is None:
        resultsdisplay = resultsdisplay.filter(accepted=False)

#return end result
    return render(request, "edit_counts.html", {"EditCountsForm": resultsdisplay})

def UpdateCountReport(request, itemid):
    resultdisplay = EditcountsqtyVariance.objects.all()
    resultdisplay = resultdisplay.filter(itemid=itemid)
    return render(request, "update_item.html", {"UpdateItemForm": resultdisplay})

def ActualUpdate(request, id, itemid):
    resultdisplay = EditcountsqtyVariance.objects.get(createdpk=id)
    form = UpdateItem(request.POST, instance=resultdisplay)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f"/dev/edit_count/{itemid}")

def MassUpdate(request):
    formset = forms.DigitalFormset()
    if request.method == 'POST':
        formset = forms.DigitalFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save()
            return HttpResponseRedirect(reverse('/dev/edit_counts/'))
    return render(request, '/dev/edit_count/', {'formset': formset})

from .forms import uploadFileModelForm

def upload(request:HttpRequest):
    if request.method == "POST":
        form = uploadFileModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('failed')
    else:
        form = uploadFileModelForm()
        return render(request, 'uploadFile.html', {'form': form})