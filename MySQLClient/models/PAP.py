#Policy And Procedures
from django.db import models
from ARH import ARH
from SI import SI
from settings import defaultCharFieldSize


class PAP(models.Model):
    # Audit ID
    AID = models.ForeignKey(
        ARH,
        on_delete=models.CASCADE
    )
    # Store ID
    SID = models.ForeignKey(
        SI,
        on_delete=models.CASCADE
    )
    # Field Name
    FNAME = models.CharField(
        max_length=defaultCharFieldSize
    )
    # Complianve Level
    COMPLVL = models.PositiveSmallIntegerField()
    # Notes
    NOTES = models.CharField(
        max_length=models.CASCADE
    )