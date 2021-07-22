"""
Simple Handlers
"""
import django.db

from main.models import snapshot, MainAuditresultsheader, UpcsScanned

#TODO Pass an audit ID here for handling the count file

def executeCountsStoredProcedureHandler(auditID: str):
    """
    Just execute the store procedure
    """

    from django.db import connection

    try:
        with connection.cursor() as cursor:
            cursor.callproc('InsertToedItCounts', [auditID])
    except Exception as E:
        print(E)
        cursor.close()
        return -1

    cursor.close()
    return 0

#TODO :: Handle UPCsScanned in Parse Handler
def modelSaveFactoryHandler(objectType: str, parsedObjects: [[str]],
                            auditID: str = None, storeNumber: str = None):
    if objectType == 'snapshot':
        instance = snapshot()
    elif objectType == 'auditresultsheader':
        instance = MainAuditresultsheader()
    elif objectType == 'upcsscanned':
        instance = UpcsScanned()
        instance.auditID = auditID
        instance.storeNumber = storeNumber
    else: return 0
    totalSaved = 0

    for object in parsedObjects:
        fields = vars(instance)
        index = 0
        for field in fields:
            if field == '_state' or field == 'id':
                continue
            if field.__contains__('date'):
                import datetime as d
                if field.__contains__('added'):
                    endIdx = object[index].index(' ')
                    date = object[index][0:endIdx]
                    object[index] = date
                else:
                    dateSplit = object[index].split('/')
                    month = int(dateSplit[0][1:])
                    day = int(dateSplit[1])
                    year = int(dateSplit[2][:-1])
                    newDate = d.date(year, month, day)
                    object[index] = newDate.__str__()

            setattr(instance, field, object[index])
            index = index + 1

        try:
            instance.save()
        except Exception as e:
            print(e)
        totalSaved = index + 1

    return totalSaved
