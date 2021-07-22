# TODO :: Transition directory creation over to Django __init__ module
# TODO :: Replace the global variable storage with 'out of view' cache
# TODO :: Transition secrets to a more secure location

from django.http import HttpRequest

def loginHandler(content, request: HttpRequest):
    """
    Will handle the user login content by acquiring it
    from the POST dictionary and placing it into persistent
    storage for future reference
    """

    import os

    from .BlobHandlers import blobDownloadHandler, blobParseHandler

    if len(content) is 0:
        # Will be caught and just return the original login page
        raise Exception


    request.session.create()

    loginValidationHandler(content['StoreNum'],
                           content['AuditID'])

    try:
        request.session['store_number'] = content['StoreNum']
        request.session['audit_id'] = content['AuditID']
    except KeyError:
        # TODO :: Handle a bad HttpRequest
        pass

    request.session['audit_in_progress'] = True

    from django.conf import settings
    from .BlobHandlers import blobUnzipHandler

    defaultBlobPath = getattr(settings, 'BLOB_DIR', None)

    if not os.path.exists(defaultBlobPath):
        os.mkdir(defaultBlobPath)

    dirName = request.session['audit_id'] + '_Snapshots'

    newClientPath = os.path.join(defaultBlobPath, dirName)
    os.mkdir(newClientPath)

    request.session['snapshot_files_path'] = newClientPath

    try:

        blobDownloadHandler(individualClientPath=newClientPath,
                            storeNumber=request.session['store_number'],
                            blobDownloadPath=newClientPath,
                            clientKey=request.session.session_key)

        unZipPath = blobUnzipHandler(zipPath=newClientPath)

        for file in os.listdir(unZipPath):
            blobParseHandler(fileName=os.path.join(unZipPath, file))

        # TODO :: Make sure counts procedure works
        #from Handlers import executeCountsStoredProcedureHandler
        #if executeCountsStoredProcedureHandler(request.session['audit_id']) == 0:
            #raise Exception

    except Exception:
        # TODO :: Create a custom exception thrown if loginHandler fails
        raise Exception

def loginValidationHandler(store_number:str, audit_id:str):
    #TODO :: Will use a DB model that will hit our table that stores Store#,AID pairs
    pass