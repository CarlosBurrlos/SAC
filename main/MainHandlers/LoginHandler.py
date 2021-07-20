# TODO :: Transition directory creation over to Django __init__ module
# TODO :: Replace the global variable storage with 'out of view' cache
# TODO :: Transition secrets to a more secure location

def loginHandler(content):
    """
    Will handle the user login content by acquiring it
    from the POST dictionary and placing it into persistent
    storage for future reference
    """

    import os
    import globals

    from .BlobHandlers import blobDownloadHandler, blobParseHandler

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
            if not blob.__contains__('Snapshot.txt'):
                continue
            result = blobParseHandler(os.path.join(defaultBlobPath, blob))
            if result == 0:
                # TODO :: Create a custom exception thrown if loginHandler().parseHandler() fails
                raise Exception
    except Exception as e:
        print(e)

    return True

