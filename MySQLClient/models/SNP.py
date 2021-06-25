# Snapshot
from django.db import models
from .ARH import ARH
class SNP(models.Model):
    # Audit ID
    AID = models.ForeignKey(
        ARH,
        on_delete=models.CASCADE
    )
    # Line number
    LNNUM = models.PositiveSmallIntegerField()
    # Item ID
    IID = models.CharField(
        max_length=10
    )
    # Size ID
    SID = models.CharField(
        max_length=10
    )
    # On Hand Qty
    OHQTY = models.PositiveIntegerField()
    # Cost
    CST = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    # Retail Price
    RP = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )