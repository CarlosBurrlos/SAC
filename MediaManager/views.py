import pathlib
import re

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from typing import List, Dict

import globals
from .Handlers import UploadHandler
from .forms import uploadFileForm


def upload(request: HttpRequest):
    # Just send the rendered template with empty form
    if request.method == "GET":
        context = {"uploadForm": uploadFileForm}
        response = render(request, "MediaForms/upload.html", context)
        return response
    else:
        form = uploadFileForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            file = request.FILES['file']
            # Our user specified path - Will commonly be just a name
            path = request.POST['Destination']
            flag, chunkswritten = UploadHandler.userUploadHandler(file, path)
            # response = f'Num Chunks Written :: {chunkswritten}'
            return HttpResponse('Succes')


from azure.storage.blob import ContainerClient, BlobProperties
from django.utils.datastructures import MultiValueDictKeyError
import os


# NOTE:: Can be modified later to handle different file names
class fileDisplay:
    def __init__(self, blobs: List[BlobProperties]):
        self.blobNames = {}
        for blob in blobs:
            nameIdx = blob.name.index('Snapshot')
            extensionIdx = blob.name.index('.')
            name = blob.name[nameIdx:extensionIdx]
            extension = blob.name[extensionIdx:]
            self.blobNames.update({name + extension: blob})

    def getDisplayNames(self):
        displayNamesList = list(self.blobNames.keys())
        return displayNamesList


def blobTestIndex(request: HttpRequest):
    if request.method == 'GET':
        # items = request.GET
        if len(request.GET) == 0:
            return render(request, "MediaForms/blobTestIndex.html")
        newDisplay = fileDisplay(blobTestList())
        try:
            if not request.GET['ListBlobs'] is None:
                context = {"blobs": newDisplay.getDisplayNames()}
                return render(request, "MediaForms/blobTestIndex.html", context)
        except MultiValueDictKeyError:
            pass
        try:
            if not request.GET['DownloadBlob'] is None:
                blobName = request.GET['BlobToDownload']
                if blobName in newDisplay.blobNames:
                    blob = newDisplay.blobNames[blobName]
                    chunksWritten = blobTestDownload(blobName, blob)
                    return HttpResponse(f'Chunks written = {chunksWritten}')
        except MultiValueDictKeyError:
            pass
        return render(request, "MediaForms/blobTestIndex.html")


def blobTestList():
    accountURI = os.getenv('AZURE_STORAGE_URI')
    containerName = os.getenv('AZURE_CONTAINER_NAME')
    key = os.getenv('AZURE_STORAGE_KEY')
    # Testing A Service Client
    # Testing A Container Client
    client = ContainerClient(accountURI, containerName, key)
    availableBlobs = [blob for blob in client.list_blobs(globals.store_num)]
    return availableBlobs


from pathlib import Path
from os import mkdir as touchDir

def blobDownloadHandler(client: ContainerClient, downloadPath, name: str, blob: BlobProperties):
    # Write to a default location

    if not os.path.exists(downloadPath.parent):
        touchDir(downloadPath)

    blobDownloadStream = client.download_blob(blob)

    chunkswritten = 0

    with open(downloadPath, 'wb+') as dest:
        for chunk in blobDownloadStream.chunks():
            chunkswritten = chunkswritten + 1
            dest.write(chunk)

    return chunkswritten


def blobTestDownload(name: str, blob: BlobProperties):
    accountURI = os.getenv('AZURE_STORAGE_URI')
    containerName = os.getenv('AZURE_CONTAINER_NAME')
    key = os.getenv('AZURE_STORAGE_KEY')

    client = ContainerClient(accountURI, containerName, key)

    downloadPath = Path.joinpath(Path(__file__).parent.parent, 'Blobs', name)
    chunksWritten = blobDownloadHandler(client, downloadPath, name, blob)
    if blobTestParse(downloadPath, name) :
        return chunksWritten
    return -1

from .models import Snapshot, Storeinformation
def blobTestParse(downloadPath, name: str):
    if name is None:
        return False
    elif name.__contains__('Snapshot.txt'):
        rule = r'\"\,|\"'
        parsedObjects = blobTestParser(downloadPath, rule)
        newSnap = Snapshot()
        for object in parsedObjects:
            newSnap.auditid = object[0]
            newSnap.storeid = object[1]
            newSnap.itemid = object[2]
            newSnap.sizeid = object[3]
            newSnap.qtyonhand = object[4]
            newSnap.cost = object[5]
            newSnap.retailprice = object[6]
            # TODO :: Replace SQLITE Model with corresponding MYSQL Model
            newSnap.save()
        return True
    elif name.__contains__('StoreInfo.txt'):
        rule = r','
        parsedObjects = blobTestParser(os.path.join(downloadPath, name), rule)
        newStoreInfo = Storeinformation()
        index = 0
        for object in parsedObjects:
            if index is 0:
                index = index + 1
                continue
            newStoreInfo.storeid = object[0]
            newStoreInfo.mallname = object[5]
            newStoreInfo.hwistoreregionid = ""
            newStoreInfo.lp_region = object[31]
            newStoreInfo.storetypeid = object[4]
            newStoreInfo.addtess = object[6]
            newStoreInfo.city = object[7]
            newStoreInfo.state = object[8]
            newStoreInfo.zip = object[9]
            newStoreInfo.save()

    elif name.__contains__('.zip'):
        # Will return the path to our unzipped files - then iterate over these and parse/upload them to DB
        unzippedFilesPath = blobTestUnzipHandler(downloadPath)
        for f in os.listdir(unzippedFilesPath):
            blobTestParse(unzippedFilesPath, f)
        os.remove(downloadPath)
        return True
    else:
        os.remove(os.path.join(downloadPath,name))
        return True

def blobTestParser(downloadPath, rule: str):
    parsedObjects = []
    # lineParser = parser.Regex(regex.compile(rule))
    with open(downloadPath, 'r+') as fileStream:
        while True:
            line = fileStream.readline()
            if line == '':
                break;
            split = re.split(rule, line)
            parsedObject = list(filter(None, split))
            parsedObjects.append(parsedObject)

    return parsedObjects

import zipfile
def blobTestUnzipHandler(downloadPath):
    #Default unzip location
    zipPath = downloadPath
    downloadPath = downloadPath.parent
    downloadPath = os.path.join(downloadPath, 'Snapshots')
    #Create if doesn't exist
    if not os.path.exists(downloadPath):
        touchDir(downloadPath)

    with zipfile.ZipFile(zipPath, 'r') as stream:
        stream.extractall(downloadPath)

    return downloadPath