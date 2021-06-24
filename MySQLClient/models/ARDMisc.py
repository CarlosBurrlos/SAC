# Audit Results Misc
from django.db import models
from ARH import ARH
from settings import defaultCharFieldSize

class ARD(models.Model):
    #Audit ID
    AID = models.ForeignKey(
        ARH,
        on_delete=models.CASCADE
    )
    #Category ID
    CID = models.CharField(
        max_length=defaultCharFieldSize
    )
    #Category
    CTG = models.CharField(
        max_length=defaultCharFieldSize
    )
    #Reason Code
    RSCODE = models.PositiveSmallIntegerField()
    #Reason Name
    RSNME = models.CharField(
        max_length=defaultCharFieldSize
    )
    #Associated Compliance Policy
    ACP = models.CharField(
        max_length=defaultCharFieldSize
    )
    #Notes
    NTS = models.CharField(
        max_length=(defaultCharFieldSize * 2)
    )
# Audit Trail
class AT(models.Model):
    #Audit ID
    AID = models.ForeignKey(
        ARH,
        on_delete=models.CASCADE
    )
    #Opened Report
    OPNRPRT = models.CharField(
        max_length=defaultCharFieldSize
    )
    #Current Audit Percentage
    CAP = models.DecimalField(
        max_length=4,
        max_digits=2
    )
    #Opened Date/Time
    ODT = models.CharField(
        max_length=defaultCharFieldSize
    )
# Audit Results Modification
class ARM(models.Model):
    #Audit ID
    AID = models.ForeignKey(
        ARH,
        on_delete=models.CASCADE
    )
    #Item ID
    IID = models.CharField(
        max_length=10
    )
    #Description
    DESC = models.TextField()
    #Modified Date/Time
    MDT = models.DateField()
# LP Auditors
class LPA(models.Model):
    STFID = models.PositiveIntegerField()
    NAME = models.CharField(
        max_length=defaultCharFieldSize
    )
