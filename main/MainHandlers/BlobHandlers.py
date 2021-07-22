import os

import django.contrib.sessions.exceptions

from .ClientHandlers import constructContainerClientHandler


def blobListHandler():
    """
    Acquires and returns a list of user readable strings
    that correspond to client blobs based on storeNum
    """
    storeNumber = 0
    containerClient = constructContainerClientHandler()
    blobsList = [str]
    for blob in containerClient.list_blobs(storeNumber):  # Prune Blob Names
        nameStartIndex = blob.name.index('Snapshot')
        extensionStartIndex = blob.name.index('.')
        name = blob.name[nameStartIndex:extensionStartIndex] + blob.name[extensionStartIndex:]
        blobsList.append(name)

    return blobsList


from azure.storage.blob import StorageStreamDownloader
from django.contrib.sessions.backends.file import SessionStore

#from importlib import import_module
#from django.conf import settings
#SessionStore = import_module(settings.SESSION_ENGINE).SessionStore


def blobDownloadHandler(individualClientPath: str, storeNumber: str, blobDownloadPath: str=None, clientKey: str=None):
    """
    Downloads all blobs for a particular storeNum
    Will be used for a complete refresh of current
    Snapshot files and at login
    """
    containerClient = constructContainerClientHandler()
    blobsToDownload = containerClient.list_blobs(storeNumber)

    if blobDownloadPath is None:
        # TODO :: Create custom exception that could be either KeyError or no session
        clientSessionStore = SessionStore(session_key=clientKey)

        # TODO :: Figure out where to download to somehow. ATM >> KeyError exception
        blobDownloadPath = clientSessionStore['storage_path']

    totalChunksDownloaded = 0

    for blob in blobsToDownload:
        blobDownloadStream: StorageStreamDownloader = containerClient.download_blob(blob)
        chunksDownloaded = 0

        newBlobPath = os.path.join(blobDownloadPath, blob.name)

        with open(newBlobPath, 'wb+') as destination:
            for chunk in blobDownloadStream.chunks():
                chunksDownloaded = chunksDownloaded + 1
                destination.write(chunk)

        if blob.name.__contains__('Snapshot.zip'):
            os.rename(newBlobPath, os.path.join(blobDownloadPath, 'Snapshot.zip'))
        else:
            os.rename(newBlobPath, os.path.join(blobDownloadPath, 'Snapshot.txt'))

        totalChunksDownloaded = totalChunksDownloaded + chunksDownloaded

    #if totalChunksDownloaded == 0:
        # TODO :: Create a custom exception thrown if blobDownloadHandler fails
        # raise Exception

    return totalChunksDownloaded


def blobDownloadFromStreamHandler(blobStream: StorageStreamDownloader):
    """
    Downloads a blob with an already existing blobStream.
    Will download to default locaiton and return number of
    chunks written
    """
    from django.conf import settings

    blobDownloadPath = getattr(settings, 'BLOB_DIR', None)
    totalChunksDownloaded = 0
    with open(os.path.join(blobDownloadPath, blobStream.name), 'wb+') as destination:
        for chunk in blobStream.chunks():
            totalChunksDownloaded = totalChunksDownloaded + 1
            destination.write(chunk)

    return totalChunksDownloaded


def specificBlobDownloadHandler(blobName: str):
    """
    Downloads a blob based off of the user specified
    name. Returns number of chunks written and stores the
    blob in the default blob location
    """
    storeNumber = 0
    containerClient = constructContainerClientHandler()
    availableBlobs = [containerClient.list_blobs(storeNumber)]
    position = [availableBlobs.index(i) for i in availableBlobs if blobName in i]
    if len(position) is not 1:
        # TODO :: Verify snap .txt and .zip only exist once for each storenum >> Throw Error
        pass
    if blobName.__contains__('Snapshot.txt') or blobName.__contains__('Snapshot.zip'):
        blob = availableBlobs[position[0]]
        blobDownloadStream = containerClient.download_blob(blob)
        chunksDownloaded = blobDownloadFromStreamHandler(blobDownloadStream)
    else:

        return -1

    return chunksDownloaded


def blobUnzipHandler(zipPath: str):
    """
    Will handle the unzipping process of a .zip blob
    if the user requests the download handler to process
    a .zip blob and return the path to unzipped directory
    """
    import zipfile

    unZipPath = os.path.join(zipPath, 'Snapshot.zip')
    # zipPath = os.path.join(blobDefaultPath, 'Snapshot')
    with zipfile.ZipFile(unZipPath, 'r') as zippedFile:
        zippedFile.extractall(zipPath)

    # FIXME :: Later on we will need to use the other files
    for file in os.listdir(zipPath):
        if not (file.__contains__('Snapshot.txt') or file.__contains__('StoreInfo.txt')):
            os.remove(os.path.join(zipPath, file))

    return zipPath


def blobParseHandler(fileName: str):
    """
    Takes in a .txt file and based on the passed rule
    will slit, parse, and return a list of parsed objects
    """

    from main.MainHandlers.Handlers import modelSaveFactoryHandler

    if fileName.__contains__('.txt'):
        # TODO :: Extend cases to handle other Snapshot files [stretch goal]
        # TODO :: Globally store rules to ease modifications
        if fileName.__contains__('Snapshot.txt'):
            rule = r'\"\,|\"'
            parsedObjects: [str] = blobParser(os.path.abspath(fileName), rule)
            saveType = 'snapshot'
        elif fileName.__contains__('StoreInfo.txt'):
            rule = r','
            parsedObjects = blobParser(fileName, rule)
            parsedObjects = parsedObjects.copy()
            parsedObjects.pop(0)
            saveType = 'auditresultsheader'

        if modelSaveFactoryHandler(saveType, parsedObjects) == 0:
            # TODO :: throw exception here
            pass

        return 1

    else:
        # TODO :: redownload once more and if retry fails cascade failure error up
        return 0


def blobParser(fileToParse: str, parseRule: str):
    import re

    parsedObjects = []
    with open(fileToParse, 'r+') as fileStream:
        lines = fileStream.readlines()
        for line in lines:
            split = re.split(parseRule, line)
            parsedObject = list(filter(lambda obj: obj is not '', split))
            parsedObject = list(filter(lambda obj: obj is not '\n', parsedObject))
            parsedObjects.append(parsedObject)

    return parsedObjects
