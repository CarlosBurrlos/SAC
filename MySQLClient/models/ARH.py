# Audit Results Header
from django.db import models
#from django.utils.translation import gettext_lazy as _
from SI import SI
#from STRClass import STRClass
#from States import States
from settings import defaultCharFieldSize

class ARH(models.Model):
    #Audit ID
    AID = models.CharField(
        max_length=10,
        primary_key=True
    )
    #Store ID
    SID = models.ForeignKey(
        SI,
        on_delete=models.CASCADE
    )
    #Store Manager
    MNGR = models.CharField(
        max_length=defaultCharFieldSize
    )
    #TODO:: [ Do we need the Audit Classification anymore? ]

    #class AuditClassificationTypes(models.TextChoices):
        #REGULAR = 'RG', _('Regular')
    #classf = models.CharField(
       # max_length=2,
       # choices=AuditClassificationTypes.choices,
       # default=AuditClassificationTypes.REGULAR
    #)

    #Added LP Measures
    ADLPMSRS = models.CharField(
        max_length=10
    )
    #YTD Sales
    YTDS = models.DecimalField(
        max_length=12,
        max_digits=2
    )
    #TODO::[May have to test for truncation]
    #YTD Sales Percentage
    YTDSP = models.DecimalField(
        max_length=4,
        max_digits=2
    )
    #YTD Comp Percentage
    YTDS_C = models.DecimalField(
        max_length=4,
        max_digits=2
    )
    #Audit Date
    DATE = models.DateField(
        auto_now=True
    )
    #Audit Type
    TYP = models.CharField(
        max_length=defaultCharFieldSize
    )
    #Auditor
    ADTR = models.CharField(
        max_size=defaultCharFieldSize
    )
    #SBA Audit
    SBA = models.DecimalField(
        max_length=12,
        max_digits=2
    )
    #Last Audit Date
    LDATE = models.DateField(
        auto_now=True
    )
    #Last Auditor
    LADTR = models.CharField(
        max_length=defaultCharFieldSize
    )
    #Last Audit Cost Adj
    LADTCADJ = models.DecimalField(
        max_length=12,
        max_digits=2
    )
    #Last Audit SBA
    LADTSBA = models.DecimalField(
        max_length=12,
        max_digits=2
    )
    #This Year Audit Count
    TYRADTCNT = models.SmallIntegerField()
    #This Year Audit Cost Adjustment
    TYRADTCSTADJ = models.DecimalField(
        max_length=12,
        max_digits=2
    )
    #Last Year Audit Count
    LYRADTCNT = models.SmallIntegerField()
    #Last Year Cost Audit Cost Adjusment
    LYRAFTCSTADJ = models.DecimalField(
        max_length=12,
        max_digits=2
    )
    #Last Year SBA
    LYRSBA = models.DecimalField(
        max_length=12,
        max_digits=2
    )
    #Region Director
    RDIR = models.CharField(
        max_length=defaultCharFieldSize
    )
    #District Manager
    DIM = models.CharField(
        max_length=defaultCharFieldSize
    )
    #Date of Audit
    DATEOA = models.DateField(auto_now=True)
    #Embroidery Units
    EMBUTS = models.PositiveIntegerField()
    #Embroidery Sales
    EMBSLS = models.PositiveIntegerField()
    #Bank Drop
    BD = models.CharField(
        max_length=5
    )
    #------------------------
    #Audit Percent
    ADTP = models.DecimalField(
        max_length=4,
        max_digits=2
    )
    #Audit Score
    ADTS = models.DecimalField(
        max_length=4,
        max_digits=2
    )