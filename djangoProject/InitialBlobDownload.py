# We will use a minimal version of the final Azure Blob Client which will allow us
# to connect and perform the initial install


class minimalBlobClient():

    # This will be a Service client - Connects to the account name
    # Therefore it will have a view of all the containers and their blobs

    def __init__(self):
        self.Temp = ''
        # Maximum chunk get size : 4MB

        # Maximum single get size : 32MB