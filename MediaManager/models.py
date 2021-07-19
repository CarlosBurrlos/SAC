
from django.db import models

class snapshot(models.Model):
    auditid = models.IntegerField(db_column='auditid', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='storeid', blank=True, null=True)  # Field name made lowercase.
    itemid = models.TextField(db_column='itemid', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.TextField(db_column='sizeid', blank=True, null=True)  # Field name made lowercase.
    qtyonhand = models.IntegerField(db_column='qtyonhand', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='cost', blank=True, null=True)  # Field name made lowercase.
    retailprice = models.FloatField(db_column='retailprice', blank=True, null=True)  # Field name made lowercase.

    class meta:
        managed = False
        db_table = 'snapshot'

class storeinformation(models.Model):
    storeid = models.IntegerField(db_column='storeid', blank=True, null=True)  # Field name made lowercase.
    mallname = models.TextField(db_column='mallname', blank=True, null=True)  # Field name made lowercase.
    hwistoreregionid = models.TextField(db_column='hwistoreregionid', blank=True, null=True)  # Field name made lowercase.
    lp_region = models.TextField(db_column='lp region', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    storetypeid = models.TextField(db_column='storetypeid', blank=True, null=True)  # Field name made lowercase.
    addtess = models.TextField(db_column='addtess', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='city', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='state', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='zip', blank=True, null=True)  # Field name made lowercase.

    class meta:
        managed = False
        db_table = 'storeinformation'