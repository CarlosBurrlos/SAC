from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.forms import model_to_dict, modelform_factory, inlineformset_factory, formset_factory
from .MainHandlers.LoginHandler import loginHandler
from .MainHandlers.LogoutHandler import logoutHandler


# Create your views here.
def login(request: HttpRequest):

    if request.method == 'GET':
        try:
            if request.session['audit_in_progress']:
                return redirect('home/')
        except KeyError:
            pass

        return render(request, 'main/login.html')

    requestContent = request.POST

    try:
        loginHandler(requestContent, request)
    except Exception as e:
        # TODO :: Log this exception and return a bad request
        return HttpResponseBadRequest

    return redirect('home/')

def home(request: HttpRequest):
    if request.method == 'GET':
        try:
            if not request.session['audit_in_progress']:
                return redirect('/')
        except KeyError:
            return redirect('/')

        if 'dest' in request.GET:
            destination = request.GET['dest']
            if destination == 'ViewReport':
                pass
            elif destination == 'Upload':
                pass
            elif destination == 'Export':
                pass
            elif destination == 'EditCounts':
                #return render(request, 'main/edit_counts.html')
                return redirect('/edit_counts/')
            elif destination == 'About':
                pass
            elif destination == 'Logout':
                logoutHandler(request)
                return redirect('/')

        return render(request, 'main/index.html')

def debugging(request: HttpRequest):
    from Debugging.DBDynamicInsert import DynamicInsertTest
    result = DynamicInsertTest(5)
    if result is not 1:
        return HttpResponse('Failed DBDynamicInsert Test')
    else:
        return HttpResponse('Passed DBDynamicInsert Test')

def editCountsReport(request: HttpRequest):
    from .models import Editcountbysku

    try:
        if not request.session['audit_in_progress']:
            return redirect('/')
    except KeyError:
        return redirect('/')

    if request.method == 'POST':
        return HttpResponseBadRequest

    audit_id = request.session['audit_id']

    countsToEdit = Editcountbysku.objects.all()

    try:
        varianceGreaterFieldValue = request.GET['VarianceGreater']
        descriptionFieldValue = request.GET['Description']
        accepted = request.GET['Accepted']
    except KeyError as e:
        print(e)
        return HttpResponseBadRequest

    # Reset since we are handling a new search

    # Reset and then return an empty form

    if descriptionFieldValue == '' or varianceGreaterFieldValue == '':
        try:
            del request.session['description']
            del request.session['greater_then']
        except KeyError:
            # We won't halt since we desire no description session val
            pass

        # Our context will be empty since we wont have had objects yet
        context = {'EditCountsForm':countsToEdit}
        return render(request, 'main/edit_counts.html', context)

    # Apply filters
    countsToEdit = countsToEdit.filter(audit_id=audit_id)
    if descriptionFieldValue != '':
        countsToEdit = countsToEdit.filter(descAription__icontains=descriptionFieldValue)
        request.session['description'] = descriptionFieldValue

    if varianceGreaterFieldValue != '':
        greaterThenVal = int(varianceGreaterFieldValue)
        lessThenVal = greaterThenVal * -1
        countsToEdit = countsToEdit.filter(
            Q(currentvariance__lt=lessThenVal) |
            Q(currentvariance__gt=greaterThenVal)
        )
        request.session['great_then'] = varianceGreaterFieldValue

    if accepted == '':
        countsToEdit = countsToEdit.filter(accepted=False)

    context = {'EditCountsForm':countsToEdit}
    return render(request,'main/edit_counts.html', context)

def UpdateCountReport(request, itemid):
    from .models import EditcountsqtyVariance
    resultdisplay = EditcountsqtyVariance.objects.filter(auditid=request.session["auditID"])
    resultdisplay = resultdisplay.filter(itemid=itemid)
    return render(request, "main/update_item.html", {"UpdateItemForm": resultdisplay})

def UpdateViolationReport(request, fieldname):
    from .models import PolicyVioloationFacts
    resultdisplay = PolicyVioloationFacts.objects.filter(fieldname=fieldname)
    return render(request, "main/update_violation.html", {"UpdateViolationForm":resultdisplay})

def ActualUpdate(request, id, itemid):
    from .models import EditcountsqtyVariance
    from .forms import UpdateItem
    resultdisplay = EditcountsqtyVariance.objects.get(createdpk=id)
    form = UpdateItem(request.POST, instance=resultdisplay)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f"/dev/edit_count/{itemid}")

def viewReport(request: HttpRequest):
    from django.forms import modelformset_factory
    from .models import MainAuditresultsheader, Departmentlossestimation, PolicyProcedures
    from .forms import PolicyStatement

    headerData = MainAuditresultsheader\
        .objects\
        .all()\
        .filter(request.session['audit_id'])

    departmentLossData = Departmentlossestimation\
        .objects\
        .all()\
        .filter(auditID=request.session['audit_id'])\
        .order_by('lostretail')

    costAdjustment = departmentLossData\
        .aggregate(costadj=Sum('lostcost'))['costAdjustment']

    auditSum = PolicyProcedures\
        .objects\
        .filter(auditid=request.session['audit_id'])

    auditSum = auditSum\
        .aggregate(auditSum=Sum('auditsum'))['auditSum']

    PolicyFormSet = modelformset_factory(model=PolicyProcedures, form=PolicyStatement, fields='__all__')

    if request.method == 'POST':
        formset = PolicyFormSet(request.POST)
        for form in formset:
            print(form.is_valid())
            if form.is_valid():
                form.save()
        return HttpResponseRedirect("/dev/report")

    alreadyExists = PolicyProcedures.objects.filter(auditid=request.session["auditID"])

    if alreadyExists.exists():
        PolicyFormSet = modelformset_factory(model=PolicyProcedures, form=PolicyStatement, fields=['fieldname', 'compliance_level', 'notes', 'auditid', 'storeid'], extra=0)
        formset = PolicyFormSet(queryset=alreadyExists)
    else:
        PolicyFormSet = modelformset_factory(model=PolicyProcedures, form=PolicyStatement, fields=['fieldname', 'compliance_level', 'notes', 'correctivetext', 'pointvalues', 'auditid', 'storeid'], extra=47)
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

    return render(request, "report.html", {"ReportResultsForm": headerData, "Costadj":costAdjustment, "DepartmentlossForm":departmentLossData, "formset": formset, "Auditsum":auditSum})


