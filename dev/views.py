from django.shortcuts import render
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import UploadFile
from .forms import uploadFileForm, UploadFileForm
from django.urls import reverse

# Create your views here.

def index(request:HttpRequest):
    return HttpResponse('Welcome to Dev Index View')

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

def uploadMultipleFiles(request:HttpRequest):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                file_instance = UploadFile(files=f)
                file_instance.save()
            redirect = reverse('uploadSuccess')
            return HttpResponseRedirect(redirect)
        else:
            form = UploadFileForm()
        return render(request, 'upload_files.html', {'form': form})
