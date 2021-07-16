import os.path
import pathlib
from django.core.files import uploadedfile
from os import makedirs as touch


# Will handle the upload of user file
# Requires a uploadedfile object wrapper of the user file
# and a path that is required to have the following format:
#   project-root/.../Uploads/[user-spec-dir]/file.upload
# within which there should exist an "Uploads" directory

# Will return a pair (path exists :: 0 || 1, number of chunks written :: n)

def userUploadHandler(file: uploadedfile, destination: str) -> (int, int):
    # Destination can be empty
    if destination is None:
        destination = "Default/"
    # Get project root
    currDir = pathlib.Path(__file__).parent
    appDir = currDir.parent
    baseDir = appDir.parent
    destinationPath = pathlib.Path().joinpath(baseDir, 'Uploads', destination)
    filePath = pathlib.Path().joinpath(destinationPath, file.name)
    flag = 0
    if not pathlib.Path(destinationPath).exists():
        touch(destinationPath)
        flag = 1
    chunksWritten = 0
    with open(filePath, 'wb+') as dest:
        for chunk in file.chunks():
            chunksWritten += 1
            dest.write(chunk)
    return flag, chunksWritten

# Will handle the download of a blob from blob storage

def blobDownloadHandler() :
    pass

# Will handle the fetching of blob storage list
def blobListHandler() :
    pass
