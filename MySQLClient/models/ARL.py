# Audit Results Line
from django.db import models
from django.utils.translation import gettext_lazy as _
from MySQLClient.models.ARH import ARH
from .SI import SI

class ARL(models.Model):
    #Created Transaction ID
    CTID = models.PositiveIntegerField(
        primary_key=True
    )
    #Audit ID
    AID = models.ForeignKey(
        ARH,
        on_delete=models.CASCADE
    )
    #Store ID
    SID = models.ForeignKey(
        SI,
        on_delete=models.CASCADE
    )

    #Add other size options
    class Sizes(models.TextChoices):
        __ =        ' ',    _('Empty')
        SMALL =     'S',    _('Small')
        MEDIUM =    'M',    _('Medium')
        LARGE =     'L',    _('Large')
        XLARGE =    'XL',   _('X-Large')
        XXLARGE =   'XXL',  _('XX-Large')
        XXXLARGE =  'XXXL', _('XXX-Large')
    #Size
    SZ = models.CharField(
        max_length=5,
        null=False
    )
    #Count QTY
    CQTY = models.PositiveIntegerField()
    #Snap QTY
    SQTY = models.PositiveIntegerField()
    #Adjustment QTY
    AQTY = models.PositiveIntegerField()
    #Retail Price
    RPRC = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    #Cost
    CST = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    #TODO :: [Verify this won't result in truncation of the Data Area ID]
    #Data Area ID
    DAID = models.PositiveIntegerField()