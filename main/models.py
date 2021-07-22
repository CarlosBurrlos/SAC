from django.db import models



class snapshot(models.Model):
    id = models.IntegerField(db_column='id', blank=True, primary_key=True)
    auditid = models.IntegerField(db_column='auditid', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='storeid', blank=True, null=True)  # Field name made lowercase.
    itemid = models.TextField(db_column='itemid', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.TextField(db_column='sizeid', blank=True, null=True)  # Field name made lowercase.
    qtyonhand = models.IntegerField(db_column='qtyonhand', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='cost', blank=True, null=True)  # Field name made lowercase.
    retailprice = models.FloatField(db_column='retailprice', blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()

    class meta:
        managed = False
        db_table = 'snapshot'

class storeinformation(models.Model):
    storeid = models.IntegerField(db_column='storeid', blank=True, null=True)  # Field name made lowercase.
    mallname = models.TextField(db_column='mallname', blank=True, null=True)  # Field name made lowercase.
    hwistoreregionid = models.TextField(db_column='hwistoreregionid', blank=True, null=True)  # Field name made lowercase.
    lp_region = models.TextField(db_column='lp region', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable Textacters.
    storetypeid = models.TextField(db_column='storetypeid', blank=True, null=True)  # Field name made lowercase.
    addtess = models.TextField(db_column='addtess', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='city', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='state', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='zip', blank=True, null=True)  # Field name made lowercase.

    class meta:
        managed = False
        db_table = 'storeinformation'

class MainAuditresultsheader(models.Model):
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.TextField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    districtcode = models.TextField(db_column='DistrictCode', blank=True, null=True)  # Field name made lowercase.
    storemanager = models.TextField(db_column='StoreManager', blank=True, null=True)  # Field name made lowercase.
    storetypeid = models.TextField(db_column='StoreTypeID', blank=True, null=True)  # Field name made lowercase.
    mailname = models.TextField(db_column='MailName', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    classification = models.TextField(db_column='Classification', blank=True, null=True)  # Field name made lowercase.
    addedlpmeasures = models.TextField(db_column='AddedLPMeasures', blank=True, null=True)  # Field name made lowercase.
    ytdsales = models.FloatField(db_column='YTDSales', blank=True, null=True)  # Field name made lowercase.
    ytdsalespct = models.FloatField(db_column='YTDSalespct', blank=True, null=True)  # Field name made lowercase.
    ytdcomppct = models.FloatField(db_column='YTDCompPct', blank=True, null=True)  # Field name made lowercase.
    auditdate = models.TextField(db_column='AuditDate', blank=True, null=True)  # Field name made lowercase.
    audittype = models.TextField(db_column='AuditType', blank=True, null=True)  # Field name made lowercase.
    auditor = models.TextField(db_column='Auditor', blank=True, null=True)  # Field name made lowercase.
    auditsba = models.FloatField(db_column='AuditSBA', blank=True, null=True)  # Field name made lowercase.
    lastauditdate = models.TextField(db_column='LastAuditDate', blank=True, null=True)  # Field name made lowercase.
    lastaudittype = models.TextField(db_column='LastAuditType', blank=True, null=True)  # Field name made lowercase.
    lastauditor = models.TextField(db_column='LastAuditor', blank=True, null=True)  # Field name made lowercase.
    lastauditcostadjusted = models.FloatField(db_column='LastAuditCostAdjusted', blank=True, null=True)  # Field name made lowercase.
    lastauditsba = models.FloatField(db_column='LastAuditSBA', blank=True, null=True)  # Field name made lowercase.
    yearsauditcount = models.IntegerField(db_column='YearsAuditCount', blank=True, null=True)  # Field name made lowercase.
    yearscostadjusted = models.FloatField(db_column='YearsCostAdjusted', blank=True, null=True)  # Field name made lowercase.
    yearssba = models.FloatField(db_column='YearsSBA', blank=True, null=True)  # Field name made lowercase.
    lastyearsauditcount = models.IntegerField(db_column='LastYearsAuditCount', blank=True, null=True)  # Field name made lowercase.
    lastyearcostadjusted = models.FloatField(db_column='LastYearCostAdjusted', blank=True, null=True)  # Field name made lowercase.
    lastyearssba = models.FloatField(db_column='LastYearsSBA', blank=True, null=True)  # Field name made lowercase.
    regionaldirector = models.TextField(db_column='RegionalDirector', blank=True, null=True)  # Field name made lowercase.
    districtmanager = models.TextField(db_column='DistrictManager', blank=True, null=True)  # Field name made lowercase.
    lpregion = models.IntegerField(db_column='LPRegion', blank=True, null=True)  # Field name made lowercase.
    dateadded = models.TextField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    embroideryunits = models.IntegerField(db_column='EmbroideryUnits', blank=True, null=True)  # Field name made lowercase.
    embroiderysales = models.FloatField(db_column='EmbroiderySales', blank=True, null=True)  # Field name made lowercase.
    bankdrop = models.TextField(db_column='BankDrop', blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'main_auditresultsheader'

class UpcsScanned(models.Model):
    # FIXME :: Will just need to go back through and append rest of model fields
    auditID = models.IntegerField()
    storeNumber = models.IntegerField()
    pass


class EditCountsBySku(models.Model):
    description = models.TextField()

    objects = models.Manager()