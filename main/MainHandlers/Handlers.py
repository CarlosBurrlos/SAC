import os
import globals


# TODO :: Transition directory creation over to Django __init__ module
# TODO :: Replace the global variable storage with 'out of view' cache
import main.models


def loginHandler(content):
    """
    Will handle the user login content by acquiring it
    from the POST dictionary and placing it into persistent
    storage for future reference
    """

    if len(content) is 0:
        raise Exception

    try:

        globals.storenum = content['StoreNum']
        globals.auditid = content['AuditID']

    except Exception:
        # TODO :: Create a custom exception thrown if loginHandler fails

        raise Exception

    from django.conf import settings

    defaultBlobPath = getattr(settings, 'BLOB_DIR', None)
    if os.path.exists(defaultBlobPath) is not True:
        os.mkdir(defaultBlobPath)
    try:
        blobDownloadHandler()
    except Exception:
        # TODO :: Create a custom exception thrown if loginHandler fails

        raise Exception
    try:
        for blob in os.listdir(defaultBlobPath):
        # Rename the files from their original format
            if blobParseHandler(os.path.join(defaultBlobPath, blob)) == 0:
                # TODO :: Create a custom exception thrown if loginHandler().parseHandler() fails
                raise Exception
    except Exception as e:
        print(e)

    return True


# TODO :: Transition secrets to a more secure location
def constructContainerClientHandler():
    """
    Accesses the stored secrets for an azure blob client
    and returns a client object
    """
    from azure.storage.blob import ContainerClient

    URI = os.getenv('AZURE_STORAGE_URI')
    containerName = os.getenv('AZURE_CONTAINER_NAME')
    key = os.getenv('AZURE_STORAGE_KEY')
    client = ContainerClient(URI, containerName, key)

    return client


# TODO :: Blob client construction


def blobListHandler():
    """
    Acquires and returns a list of user readable strings
    that correspond to client blobs based on storeNum
    """
    storeNumber = globals.storenum
    containerClient = constructContainerClientHandler()
    blobsList = [str]
    for blob in containerClient.list_blobs(storeNumber):  # Prune Blob Names
        nameStartIndex = blob.name.index('Snapshot')
        extensionStartIndex = blob.name.index('.')
        name = blob.name[nameStartIndex:extensionStartIndex] + blob.name[extensionStartIndex:]
        blobsList.append(name)

    return blobsList


from azure.storage.blob import StorageStreamDownloader


def blobDownloadHandler():
    """
    Downloads all blobs for a particular storeNum
    Will be used for a complete refresh of current
    Snapshot files and at login
    """
    from django.conf import settings

    storeNumber = globals.storenum
    containerClient = constructContainerClientHandler()
    blobsToDownload = containerClient.list_blobs(storeNumber)
    blobDownloadPath = getattr(settings, 'BLOB_DIR', None)
    totalChunksDownloaded = 0
    for blob in blobsToDownload:
        blobDownloadStream: StorageStreamDownloader = containerClient.download_blob(blob)
        chunksDownloaded = 0
        with open(os.path.join(blobDownloadPath, blob.name), 'wb+') as destination:
            for chunk in blobDownloadStream.chunks():
                chunksDownloaded = chunksDownloaded + 1
                destination.write(chunk)
        if blob.name.__contains__('Snapshot.zip'):
            path = os.path.join(blobDownloadPath, blob.name)
            newPath = os.path.join(blobDownloadPath, 'Snapshot.zip')
            os.rename(path, newPath)

        totalChunksDownloaded = totalChunksDownloaded + chunksDownloaded

    if totalChunksDownloaded == 0:
        # TODO :: Create a custom exception thrown if blobDownloadHandler fails
        raise Exception

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


def sBlobDownloadHandler(blobName: str):
    """
    Downloads a blob based off of the user specified
    name. Returns number of chunks written and stores the
    blob in the default blob location
    """
    storeNumber = globals.storenum
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


def blobUnzipHandler():
    """
    Will handle the unzipping process of a .zip blob
    if the user requests the download handler to process
    a .zip blob and return the path to unzipped directory
    """
    import zipfile
    from django.conf import settings

    blobDefaultPath = getattr(settings, 'BLOB_DIR', None)
    unZipPath = os.path.join(blobDefaultPath, 'Snapshot.zip')
    zipPath = os.path.join(blobDefaultPath, 'Snapshot')
    with zipfile.ZipFile(unZipPath, 'r') as zippedFile:
        zippedFile.extractall(zipPath)

    return zipPath


def blobParseHandler(fileName: str):
    """
    Takes in a .txt file and based on the passed rule
    will slit, parse, and return a list of parsed objects
    """

    # TODO :: Test map() w/ lambda function optimization [below]
    # snapsToSave = map(lambda: Snapshot: Snapshot.__init__(), parsedObjects
    # for snap in snapsToSave:
    #   snap.save()

    def transform(A: [[]]):
        """
        Will transform parsed list of objects into individual lists
        for passing to our lambda function
        Will return our list of new argument lists
        """

        B = []
        i = 0
        z = len(A)
        y = len(A[0]) - 1
        for j in range(0, y, 1):
            B.append([A[i][j] for i in range(0, z, 1)])

        return B

    from main.models import modelSaveFactory

    if fileName.__contains__('.txt'):
        # TODO :: Extend cases to handle other Snapshot files [stretch goal]
        if fileName.__contains__('Snapshot.txt'):
            # TODO :: Globally store rules to ease modifications
            rule = r'\"\,|\"'
            parsedObjects: [str] = blobParser(os.path.abspath(fileName), rule)
            saveType = 'snapshot'
            # TODO :: Figure out how to use the lambda to create list of objects

            #args = transform(parsedObjects)
            #itemsToSave = map(lambda snapshot: snapshot.stage(), args[0], args[1], args[2], args[3], args[4], args[5])
        else:
            rule = r','
            parsedObjects = blobParser(fileName, rule)
            parsedObjects.pop(0)
            saveType = 'auditresultsheader'

        if modelSaveFactory(saveType, parsedObjects) == 0:
            # TODO :: throw exception here
            pass

        return 1

    elif fileName.__contains__('.zip'):
        unZipPath = blobUnzipHandler()
        storeInfoPath = ''
        for file in os.listdir(unZipPath):
            if file.__contains__('StoreInfo'):
                storeInfoPath = file
            else:
                os.remove(os.path.join(unZipPath,file))

        return blobParseHandler(os.path.join(unZipPath,storeInfoPath))

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
            parsedObjects.append(parsedObject)

    return parsedObjects


# TODO :: handle upload of user files
def uploadHandler():
    """
    Handles an individual user uploaded file and returns
    its path which will be used to perform parsing
    """
    pass


# TODO:: handle parsing of client uploaded file
def uploadParseHandler():
    """
    Handles the writting to project file system
    of a user file to be uploaded to the default upload
    location
    """
    pass
