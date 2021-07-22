import os

from main.models import snapshot, MainAuditresultsheader
from django.http import HttpRequest

def logoutHandler(request: HttpRequest):
    try:
        snapshotFilePath = request.session['snapshot_files_path']
    except KeyError:
        raise Exception

    for file in os.listdir(snapshotFilePath):
        os.remove(os.path.join(snapshotFilePath, file))
    os.rmdir(snapshotFilePath)

    request.session['audit_in_progress'] = False

    snapshot.objects.filter(storeid=request.session['store_number']).delete()
    MainAuditresultsheader.objects.filter(auditid=request.session['audit_id']).delete()

    del request.session['audit_id']
    del request.session['store_number']
    del request.session['snapshot_files_path']