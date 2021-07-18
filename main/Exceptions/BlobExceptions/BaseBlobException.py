from azure.storage.blob import BlobProperties


class BaseBlobException(Exception):
    """
    BaseBlobException is the root exception.
    It includes basic blob information fields that aid in
    identifying the offending blob or other meta data.
    """

    def __init__(self, offendingClient: int, blob: BlobProperties = None, msg: str = None):
        """
        __init__(...,blob: BlobProperties, msg:str)
        BaseBlobException will take a message (msg) and BlobProperties (blob)
        offendingClient will be the individual Auditors ID
        """
        super().__init__()

        if offendingClient is None:
            # TODO :: Figure out how we would handle an empty offendingClient ID
            # >> Would this ever happen?
            pass
        else:
            self.auditorID = offendingClient

        self.msg = msg

        if blob is None:
            self.msg = f"Offending Auditor: {self.auditorID}\n"
            self.msg = f"No Blob information to display\n"
        else:
            self.blobName = blob.name
            self.blobSize = blob.size
            self.DOC = blob.creation_time
            self.lastModified = blob.last_modified
            if msg is None:
                self.msg = f"Problem with blob: {self.blobName}\n"
                self.msg += f"Blob: {self.blobName} has size: {self.blobSize}\n"
                self.msg += "Other Blob Information:\n"
                self.msg += f"\tDOC: {self.DOC}\n"
                self.msg += f"\tLast Modified: {self.lastModified}\n"
                self.msg += f"Client ID: {offendingClient}\n"
