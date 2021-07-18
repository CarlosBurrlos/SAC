from django.db import models

class snapshot(models.model):
    auditid = models.integerfield(db_column='auditid', blank=true, null=true)  # field name made lowercase.
    storeid = models.integerfield(db_column='storeid', blank=true, null=true)  # field name made lowercase.
    itemid = models.textfield(db_column='itemid', blank=true, null=true)  # field name made lowercase.
    sizeid = models.textfield(db_column='sizeid', blank=true, null=true)  # field name made lowercase.
    qtyonhand = models.integerfield(db_column='qtyonhand', blank=true, null=true)  # field name made lowercase.
    cost = models.floatfield(db_column='cost', blank=true, null=true)  # field name made lowercase.
    retailprice = models.floatfield(db_column='retailprice', blank=true, null=true)  # field name made lowercase.

    class meta:
        managed = false
        db_table = 'snapshot'

class storeinformation(models.model):
    storeid = models.integerfield(db_column='storeid', blank=true, null=true)  # field name made lowercase.
    mallname = models.textfield(db_column='mallname', blank=true, null=true)  # field name made lowercase.
    hwistoreregionid = models.textfield(db_column='hwistoreregionid', blank=true, null=true)  # field name made lowercase.
    lp_region = models.textfield(db_column='lp region', blank=true, null=true)  # field name made lowercase. field renamed to remove unsuitable characters.
    storetypeid = models.textfield(db_column='storetypeid', blank=true, null=true)  # field name made lowercase.
    addtess = models.textfield(db_column='addtess', blank=true, null=true)  # field name made lowercase.
    city = models.textfield(db_column='city', blank=true, null=true)  # field name made lowercase.
    state = models.textfield(db_column='state', blank=true, null=true)  # field name made lowercase.
    zip = models.textfield(db_column='zip', blank=true, null=true)  # field name made lowercase.

    class meta:
        managed = false
        db_table = 'storeinformation'