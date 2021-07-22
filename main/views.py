from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse
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
    from .models import EditCountsBySku

    try:
        if not request.session['audit_in_progress']:
            return redirect('/')
    except KeyError:
        return redirect('/')

    if request.method == 'POST':
        return HttpResponseBadRequest

    audit_id = request.session['audit_id']

    countsToEdit = EditCountsBySku.objects.all()

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