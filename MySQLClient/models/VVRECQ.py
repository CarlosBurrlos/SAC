# Variance Verification
from django.db import models
from ARH import ARH
from settings import defaultCharFieldSize


# Variance Verification Report QTY
class VVRECQ(models.Model):
    # Audit ID
    AID = models.ForeignKey(
        ARH,
        on_delete=models.CASCADE
    )
    # Item ID
    IID = models.CharField(
        max_length=10
    )
    # Description
    DESC = models.CharField(
        max_length=(defaultCharFieldSize * 2)
    )
    # Snap Qty
    SNPQTY = models.PositiveIntegerField()
    # Original Count
    OGCNT = models.PositiveIntegerField()
    # Current Count
    CURRCNT = models.PositiveIntegerField()
    # TODO :: [Check that this is desired to be a boolean field]
    # Modified
    MOD = models.BooleanField()
    # TODO :: [Check that this is desired to be a boolean field]
    # Accepted
    ACP = models.BooleanField()
