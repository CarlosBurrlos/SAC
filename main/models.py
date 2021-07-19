from django.db import models

def modelSaveFactory(objectType: str, parsedObjects: [[str]]):
    if objectType == 'snapshot':
        instance = snapshot()
    elif objectType == 'auditresultsheader':
        instance = auditresultsheader()
    else: return 0
    totalSaved = 0

    for object in parsedObjects:
        fields = vars(instance)
        index = 0
        for field in fields:
            if field == '_state' or field == 'id':
                continue
            if field.__contains__('date'):
                import datetime as d
                dateSplit = object[index].split('/')
                month = int(dateSplit[0][1:])
                day = int(dateSplit[1])
                year = int(dateSplit[2][:-1])
                newDate = d.date(year, month, day)
                field = newDate.__str__()

            setattr(instance, field, object[index])
            index = index + 1

        instance.save()
        totalSaved = index + 1

    return totalSaved

class snapshot(models.Model):
    auditid = models.IntegerField(db_column='auditid', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='storeid', blank=True, null=True)  # Field name made lowercase.
    itemid = models.TextField(db_column='itemid', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.TextField(db_column='sizeid', blank=True, null=True)  # Field name made lowercase.
    qtyonhand = models.IntegerField(db_column='qtyonhand', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='cost', blank=True, null=True)  # Field name made lowercase.
    retailprice = models.FloatField(db_column='retailprice', blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager

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

class auditresultsheader(models.Model):
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    districtcode = models.CharField(db_column='DistrictCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    storemanager = models.CharField(db_column='StoreManager', max_length=45, blank=True, null=True)  # Field name made lowercase.
    storetypeid = models.CharField(db_column='StoreTypeID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mailname = models.CharField(db_column='MailName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=120, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    classification = models.CharField(db_column='Classification', max_length=45, blank=True, null=True)  # Field name made lowercase.
    addedlpmeasures = models.CharField(db_column='AddedLPMeasures', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ytdsales = models.DecimalField(db_column='YTDSales', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ytdsalespct = models.DecimalField(db_column='YTDSalesPct', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ytdcomppct = models.DecimalField(db_column='YTDCompPct', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    auditdate = models.DateField(db_column='AuditDate', blank=True, null=True)  # Field name made lowercase.
    audittype = models.CharField(db_column='AuditType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    auditor = models.CharField(db_column='Auditor', max_length=120, blank=True, null=True)  # Field name made lowercase.
    auditsba = models.DecimalField(db_column='AuditSBA', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastauditdate = models.DateField(db_column='LastAuditDate', blank=True, null=True)  # Field name made lowercase.
    lastaudittype = models.CharField(db_column='LastAuditType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastauditor = models.CharField(db_column='LastAuditor', max_length=120, blank=True, null=True)  # Field name made lowercase.
    lastauditcostadjusted = models.DecimalField(db_column='LastAuditCostAdjusted', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastauditsba = models.DecimalField(db_column='LastAuditSBA', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    yearsauditcount = models.IntegerField(db_column='YearsAuditCount', blank=True, null=True)  # Field name made lowercase.
    yearscostadjusted = models.DecimalField(db_column='YearsCostAdjusted', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    yearssba = models.DecimalField(db_column='YearsSBA', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastyearsauditcount = models.IntegerField(db_column='LastYearsAuditCount', blank=True, null=True)  # Field name made lowercase.
    lastyearscostadjusted = models.DecimalField(db_column='LastYearsCostAdjusted', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastyearssba = models.DecimalField(db_column='LastYearsSBA', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    regionaldirector = models.CharField(db_column='RegionalDirector', max_length=120, blank=True, null=True)  # Field name made lowercase.
    districmanager = models.CharField(db_column='DistricManager', max_length=120, blank=True, null=True)  # Field name made lowercase.
    lpregion = models.IntegerField(db_column='LPRegion', blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    embroideryunits = models.IntegerField(db_column='EmbroideryUnits', blank=True, null=True)  # Field name made lowercase.
    embroiderysales = models.DecimalField(db_column='EmbroiderySales', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bankdrop = models.CharField(db_column='BankDrop', max_length=45, blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager

    class Meta:
        managed = False
        db_table = 'auditresultsheader'