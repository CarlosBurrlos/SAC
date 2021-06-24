# Store Information
from django.db import models
from settings import defaultCharFieldSize
from States import States

class SI (models.Model):
    #Store ID
    SID = models.PositiveIntegerField(
        primary_key=True,
        null=False
    )
    #Mall Name
    MLNM = models.CharField(
        max_length = defaultCharFieldSize,
        null=False
    )
    #HWI Store Region ID
    HWIRID = models.PositiveIntegerField(
        null=False
    )
    #HWI Store District ID
    HWIDID = models.PositiveIntegerField(
        null=False
    )
    # LP Region
    LPR = models.CharField(
        max_length=10
    )
    #District Code
    DC = models.CharField(
        max_length=10
    )
    #Store Type ID
    STID = models.PositiveIntegerField(
        null=False
    )
    #Address
    ADDR = models.CharField(
        max_length=defaultCharFieldSize
    )
    #City
    CTY = models.CharField(
        max_length=defaultCharFieldSize
    )
    #Zipcode
    ZIP = models.PositiveIntegerField(
        null=False
    )
    #State
    ST = models.CharField(
        max_length=2,
        choices=States.choices,
        default=States.__
    )