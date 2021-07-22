from django.shortcuts import render
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Snapshot, VarianceReport, EditcountsqtyVariance, Editcountbysku, Auditresultsheader, Departmentlossestimation, PolicyProcedures, PolicyViolationFacts, PolicyViolations, PolicyViolationsView
from .forms import uploadFileForm, UpdateItem, uploadFileModelForm, PolicyStatement, PolicyViolation
from django.forms import modelformset_factory, model_to_dict, modelform_factory, inlineformset_factory, formset_factory
from django.urls import reverse
from django.db.models import Q, Sum
from django import forms
# Create your views here.

PolicyChoices = [
    (10, 'A'),
    (5, 'NA'),
    (0, 'UA')
]

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
    response = render(request, 'DevIndex.html')
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

def set(request):
    return HttpResponse("Note:: SAC is note handling SET requests at the moment\n")


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
    storeID = request.GET.get('StoreID')
    greaterthen = request.GET.get('VarianceGreater')
    description = request.GET.get('Description')
    accepted = request.GET.get('Accepted')

    #Checking to see if all variances that are greater then 3 have been accepted. If not
    variancegreater = Editcountbysku.objects.filter(Q(currentvariance__lt=-3) | Q(currentvariance__gt=3))
    variancegreater = variancegreater.filter(auditid=request.session["auditID"])
    variancegreater = variancegreater.filter(accepted=False)

    greaterthenwarning = ""

    if variancegreater.exists():
        greaterthenwarning = "You must accept all items that have a variance greater then 3.\r\n To do this please update at least on item under specified SKU's."

    if storeID != "" and storeID is not None:
        request.session["storeID"] = storeID

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

    if accepted != "" and accepted is not None:
        if accepted == "on":
            accepted = "True"
            resultsdisplay = resultsdisplay.filter(accepted=accepted)

    elif accepted is None:
        resultsdisplay = resultsdisplay.filter(accepted=False)

#return end result
    return render(request, "edit_counts.html", {"EditCountsForm": resultsdisplay, "GreaterThenWarning":greaterthenwarning})

def UpdateCountReport(request, itemid):
    resultdisplay = EditcountsqtyVariance.objects.filter(auditid=request.session["auditID"])
    resultdisplay = resultdisplay.filter(itemid=itemid)
    return render(request, "update_item.html", {"UpdateItemForm": resultdisplay})

def ActualUpdate(request, id, itemid):
    resultdisplay = EditcountsqtyVariance.objects.get(createdpk=id)
    form = UpdateItem(request.POST, instance=resultdisplay)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f"/dev/edit_count/{itemid}")

def ActualUpdateViolation(request):
    # Delete Current Violations
    PolicyViolations.objects.filter(auditid=request.session["auditID"]).delete()

    violationformset = modelformset_factory(model=PolicyViolations, form=PolicyViolation, fields=['auditid', 'storeid', 'fieldname', 'violationdescription', 'correctivetext', 'pointvalues', 'reason'])
    if request.method == 'POST':
        formset = violationformset(request.POST)
        for form in formset:
            if form.is_valid():
                form.save()
        return HttpResponseRedirect("/dev/report/")

def AuditReportViewer(request):
    #Checking to see if all variances that are greater then 3 have been accepted. If not
    variancegreater = Editcountbysku.objects.filter(Q(currentvariance__lt=-3) | Q(currentvariance__gt=3))
    variancegreater = variancegreater.filter(auditid=request.session["auditID"])
    variancegreater = variancegreater.filter(accepted=False)

    if variancegreater.exists():
        request.session["description"] = ""
        request.session["greaterthen"] = 3
        greaterthenwarning = "You must accept all items that have a variance greater then 3.\r\n To do this please update at least on item under specified SKU's."
        return render(request, "edit_counts.html", {"EditCountsForm": variancegreater, "GreaterThenWarning":greaterthenwarning})

    # Setting the initials for the forms if not already submitted

    # Getting the Information for the top section of the report
    resultdisplay = Auditresultsheader.objects.all()
    resultdisplay = resultdisplay.filter(auditid=request.session["auditID"])

    # Getting the Department Loss Estimation and ordering by ascending
    departmentloss = Departmentlossestimation.objects.all()
    departmentloss = departmentloss.filter(auditid=request.session["auditID"]).order_by('lostcost')

    # Creation of single variable that is our adj lost cost
    costadj = departmentloss.aggregate(costadj=Sum('lostcost'))['costadj']

    # Creation of AuditScroe
    auditsum = PolicyProcedures.objects.filter(auditid=request.session["auditID"])
    auditsum = auditsum.aggregate(auditsum=Sum('auditsum'))['auditsum']

    #Create Base Formset for PolicyFormsets
    PolicyFormSet = modelformset_factory(model=PolicyProcedures, form=PolicyStatement, fields='__all__')

    #If it was a post then do below
    if request.method == 'POST':
        #Create empty array for field names
        fieldnamearray = []
        #Grab what was posted
        formset = PolicyFormSet(request.POST)
        #if form inside formset is valid then save
        #and if forms compliance_level is UA then append the fieldname to our empty array
        for form in formset:
            if form.is_valid():
                fieldname = form.cleaned_data["fieldname"]
                compliance_level = form.cleaned_data["compliance_level"]
                if compliance_level == "UA":
                    fieldnamearray.append(fieldname)
                form.save()
        #Create Q object for OR querysets
        q_object = Q()
        #Take all fieldnames that were UA and make an OR queryset to grab all related items
        for field in fieldnamearray:
            q_object |= Q(fieldname=field)
        #get those values and append extra information into the dictionaries and place into array that way we can use it for intial data.
        resultdisplay = PolicyViolationFacts.objects.filter(q_object).values()
        list = []
        for dict in resultdisplay:
            del dict['id']
            dict['auditid'] = request.session["auditID"]
            dict['storeid'] = request.session["storeID"]
            dict['reason'] = False
            list.append(dict)
        #Make the UA
        policyviolationformset = modelformset_factory(model=PolicyViolations, form=PolicyViolation, fields=['auditid', 'storeid', 'fieldname', 'violationdescription', 'correctivetext', 'pointvalues', 'reason'], extra= len(list))
        formset = policyviolationformset(queryset=PolicyViolations.objects.none(), initial=list)
        if fieldnamearray:
            return render(request, "update_violation.html", {"formset": formset})
        else:
            return HttpResponseRedirect("/dev/report/")

    alreadyexists = PolicyProcedures.objects.filter(auditid=request.session["auditID"])

    if alreadyexists.exists():
        PolicyFormSet = modelformset_factory(model=PolicyProcedures, form=PolicyStatement, fields=['fieldname', 'compliance_level', 'notes', 'auditid', 'correctivetext', 'pointvalues', 'storeid'], extra=0)
        formset = PolicyFormSet(queryset=alreadyexists)
    else:
        PolicyFormSet = modelformset_factory(model=PolicyProcedures, form=PolicyStatement, fields=['fieldname', 'compliance_level', 'notes', 'auditid', 'correctivetext', 'pointvalues', 'storeid'], extra=47)
        formset = PolicyFormSet(queryset=PolicyProcedures.objects.none(), initial=[
        {
            'pointvalues': 15,
            'correctivetext': 'I-E',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Corporate Giving',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'I-D',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Dress Code',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'I-A',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Employee Purchases',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'IV-A',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Information Center',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'IV-B',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Paperwork Retention',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'II-C',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Sales Floor',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'I-B',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Scheduling',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'VI-B',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Supplies',
        },
        {
            'pointvalues': 10,
            'correctivetext': 'I-J',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Time Card',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'I-C',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Training',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'V-F',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Clubhouse Trade',
        },
        {
            'pointvalues': 3,
            'correctivetext': 'V-E',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Customization',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'V-G',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Customizing Outside',
        },
        {
            'pointvalues': 3,
            'correctivetext': 'V-A',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Defects',
        },
        {
            'pointvalues': 5,
            'correctivetext': 'VI-D',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Embroidery Machine',
        },
        {
            'pointvalues': 3,
            'correctivetext': 'V-B',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Price Changes',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'V-D',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Receiving',
        },
        {
            'pointvalues': 3,
            'correctivetext': 'V-C',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Transfers',
        },
        {
            'pointvalues': 6,
            'correctivetext': 'II-B',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Access Pass',
        },
        {
            'pointvalues': 0,
            'correctivetext': 'III-B',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Bank Deposits',
        },
        {
            'pointvalues': 0,
            'correctivetext': 'III-O',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Cancels',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'III-D',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Cash Over/Short',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'II-A',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Cash Wrap',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'III-P',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Counterfeits',
        },
        {
            'pointvalues': 7,
            'correctivetext': 'III-G',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Credit Cards',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'III-F',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Daily Paperwork',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'III-R',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Discounts',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'III-C',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Gift Cards',
        },
        {
            'pointvalues': 7,
            'correctivetext': 'III-I',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Manual Sales',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'III-A',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Mid-Day Bank Drop',
        },
        {
            'pointvalues': 0,
            'correctivetext': 'III-J',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'No Sales',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'III-K',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Payouts/PayIns',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'III-O',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Post Voids',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'III-L',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Returns/Exchanges',
        },
        {
            'pointvalues': 7,
            'correctivetext': 'III-M',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Shift Changes',
        },
        {
            'pointvalues': 5,
            'correctivetext': 'III-N',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Traveler\'s Checks',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'III-O',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Voided Lines',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'II-D',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Web Orders',
        },
        {
            'pointvalues': 4,
            'correctivetext': 'VIII-A',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Audit Prep',
        },
        {
            'pointvalues': 4,
            'correctivetext': 'VIII-C',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'External Theft',
        },
        {
            'pointvalues': 15,
            'correctivetext': 'VIII-D',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Internal Counts',
        },
        {
            'pointvalues': 2,
            'correctivetext': 'VII-B',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Refuse Disposal',
        },
        {
            'pointvalues': 10,
            'correctivetext': 'VI-A',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Repair and Maintenance',
        },
        {
            'pointvalues': 4,
            'correctivetext': 'VIII-E',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Restitution',
        },
        {
            'pointvalues': 5,
            'correctivetext': 'VIII-H',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Safes',
        },
        {
            'pointvalues': 5,
            'correctivetext': 'VIII-H',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Security Equipment',
        },
        {
            'pointvalues': 5,
            'correctivetext': 'VIII-F',
            'storeid': request.session["storeID"],
            'auditid': request.session["auditID"],
            'fieldname': 'Store Keys',
        }
    ])

    ViolationResults = PolicyViolationsView.objects.filter(auditid=request.session["auditID"])

    fieldarray = ['Employee Purchases', 'Sales Floor', 'Time Card', 'Customizing Outside', 'Price Changes', 'Cancels', 'Counterfeits', 'Discounts', 'Mid-Day Bank Drop', 'Post Voids', 'Traveler\'s Checks', 'Internal Counts', 'Safes']

    return render(request, "report.html", {"ReportResultsForm": resultdisplay, "Costadj":costadj, "DepartmentlossForm":departmentloss, "formset": formset, "Auditsum":auditsum, "Fieldarray":fieldarray, "ViolationResults":ViolationResults})

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