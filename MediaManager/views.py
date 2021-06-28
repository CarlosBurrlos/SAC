from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import uploadFileForm as upff
from pathlib import Path
import os

requestOptions=[
    # Dev request options
    "load_from_local ::  POST a file from local with a given [path] string",
    "get_file :: GET information from an uploaded file"
    # More request options to come
]

def handleLocalFileUpload(uploadFile):
    with open(
            os.path.join((Path(os.getcwd()).parent), 'tempUpload.txt'), 'rb+') as dest:
        for chunk in uploadFile.chunks():
            dest.write(chunk)

# Create your views here.
def index(request:HttpRequest):
    return HttpResponse('Handle File Upload View loaded')

def file(request:HttpRequest):
    if request.method is not 'GET' or request.method is not 'POST':
        return HttpResponse(request.path + 'Only accepts GET or POST requests')
    else:
        return localFileUpload(request)

def localFileUpload(request:HttpRequest):
    # If we are handling a get_file
    if request.method == 'GET':
        # Our store upload file information form
        form = upff()
        # Render our form in a response
        return render(request, 'getLocalFileForm.html', {'form':form})
    # If we are handling a load_from_local
    elif request.method == 'POST':
        form = upff(request.POST)
        if form.is_valid():
            handleLocalFileUpload(request.FILES['temp.txt'])
            return HttpResponseRedirect('/')


