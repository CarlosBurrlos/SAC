import django.http
from django.shortcuts import render
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import uploadFileForm
from pathlib import Path

# Create your views here.

def index(request:HttpRequest):
    return HttpResponse('Welcome to Dev Index View')

def handleFileUpload(file:UploadedFile):
    print('here')
    with open(
        'temp.txt'
        'wb+'
    ) as dest:
        for chunk in file.chunks():
            dest.write(chunk)

# TODO :: Setup some sort of fall back to handle this information
def upload(request:HttpRequest):
    if request.method is 'POST':
        form = uploadFileForm(request.FILES)
        if form.is_valid():
            handleFileUpload(request.FILES['upload'])
            return HttpResponseRedirect('uploadSuccess/')
    else:
        form = uploadFileForm()
        return render(request, 'uploadFile.html', {'form': form})

def uploadSuccess(request:HttpRequest):
    return HttpResponse('File Successfully uploaded')
