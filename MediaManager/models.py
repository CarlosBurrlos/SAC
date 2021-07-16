from django.db import models

class Snapshot(models.Model):
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.TextField(db_column='ItemID', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.TextField(db_column='SizeID', blank=True, null=True)  # Field name made lowercase.
    qtyonhand = models.IntegerField(db_column='QtyOnHand', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    retailprice = models.FloatField(db_column='RetailPrice', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'snapshot'

class Storeinformation(models.Model):
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    mallname = models.TextField(db_column='MallName', blank=True, null=True)  # Field name made lowercase.
    hwistoreregionid = models.TextField(db_column='HWIStoreRegionID', blank=True, null=True)  # Field name made lowercase.
    lp_region = models.TextField(db_column='LP Region', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    storetypeid = models.TextField(db_column='StoreTypeID', blank=True, null=True)  # Field name made lowercase.
    addtess = models.TextField(db_column='Addtess', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storeinformation'