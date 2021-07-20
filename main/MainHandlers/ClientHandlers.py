def constructContainerClientHandler():
    """
    Accesses the stored secrets for an azure blob client
    and returns a client object
    """

    import os

    from azure.storage.blob import ContainerClient

    URI = os.getenv('AZURE_STORAGE_URI')
    containerName = os.getenv('AZURE_CONTAINER_NAME')
    key = os.getenv('AZURE_STORAGE_KEY')
    client = ContainerClient(URI, containerName, key)

    return client


# TODO :: Blob client construction
