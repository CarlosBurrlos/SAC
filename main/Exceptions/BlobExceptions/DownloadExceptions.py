from .BaseBlobException import BaseBlobException

class BaseDownloadException(BaseBlobException):

    """Priority :: Average"""

    """Possible Cause :: Invalid keys/access"""

    """
    Thrown if a client cannot be created. Client type
    will be included in msg data and desired container/blob
    will be too boot.
    Further download exception messages/components will be
    built off of the base exception knowing the client type
    and reason for failure
    """

    def __init__(self, CID, blob, msg: str, clientType: str = "Container",
                 downloadAttempt: int = 1):

        super().__init__(CID, blob, msg)

        self.clientType = clientType
        self.attempts = downloadAttempt

        if self.attempts is not 1:
            # Priority increases
            self.msg = f"Priority Level :: {self.attempts}\n"
        else:
            self.msg = f"Initial Download Attempt\n"

        self.msg += f"Client of type {clientType} attempted to download {blob.name}\n"

class NoBlobsDownloadException(BaseDownloadException):

    """Priority :: Very High"""

    """Possible Cause :: Blob was removed, overwritten, or never existed"""

    """
    Thrown when the client wishes to download their blobs
    either at login or on request after login and there
    are no blobs for their respective auditID
    """

    def __init__(self, CID, msg: str, containerName: str,
                 containerLastModified: str, containerProperties: str):

        super().__init__(CID, msg)

        self.msg += f"Failed to download blobs from {containerName}\n"
        self.msg += f"No blobs found in {containerName}\n"
        self.msg += f"Container was last modified on {containerLastModified}\n"
        self.msg += f"Container properties include {containerProperties}\n"


class BlobStreamDownloadException(BaseDownloadException):

    """Priority :: Average"""

    """Possible Cause :: TBD"""

    """
    Thrown when unable to create a stream from download-blob-like
    methods.
    Also thrown if the download stream fails/breaks
    """

    def __init__(self, CID, blob, msg:str, flag: int = 0):
        super().__init__(CID, blob, msg)
        if flag is 0:
            self.msg += "Blob Stream Download Exception caused by failure to\n\tcreate download" \
                        f"stream for client ID: {CID} for blob: {blob.name}\n"
            self.msg += f"Please check the container/blob permissions for client ID: {CID}\n"
            self.msg += f"Or check that the container is not being held in a lease at the moment\n"
            self.msg += "For other issues review the azure.storage.blob documentation on the Azure sdk portal\n"
        else:
            self.msg += "Blob Stream Download Exception caused by broken download stream fault\n"
            self.msg += f"Check that the desired blob ({blob.name}) still exists or that permissions haven't changed\n"

class MultipleBlobInstancesDownloadException(BaseDownloadException):

    """Priority :: Very High"""

    """Possible Cause :: Container maintenance failure"""

    """
    Thrown when a client goes to download their blobs but there
    exist multiple instances for their respective ID
    This could result from containers not being kept up to date
    or recycling fails to execute properly
    """

    def __init__(self, CID, container: str, blobs: [str]):
        super(CID)
        self.msg += f"Client ID: {CID} accessed container {container}\n"
        self.msg += f"However, excess blobs were found ({len(blobs)})\n"
        for blob in blobs:
            self.msg += f"Blob: {blob.name} was downloaded\n"

class UnwantedBlobsDownloadedException(MultipleBlobInstancesDownloadException):

    """Priority :: Case-by-Case"""

    """
    Thrown when a client downloads unnecessary blobs that are neither
    snapshot.txt or snapshot.zip
    Also thrown if somehow the client downloads multiple Blobs for their
    given ID
    """

    def __init__(self, CID, container, blobs, storeNumber: str):
        super().__init__(CID, container, blobs)
        self.msg += "However, neither Snapshot.txt or Snapshot.zip were downloaded" \
            f"for store number: {storeNumber}"
