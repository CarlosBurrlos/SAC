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

class VarianceReport(models.Model):
    id = models.AutoField(primary_key=True, db_column='AuditId')
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.CharField(db_column='ItemID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sizeid = models.CharField(db_column='SizeID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    scannedqty = models.IntegerField(db_column='ScannedQty', blank=True, null=True)  # Field name made lowercase.
    qtyonhand = models.IntegerField(db_column='QtyOnHand', blank=True, null=True)  # Field name made lowercase.
    varianceqty = models.IntegerField(db_column='VarianceQty', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.DecimalField(db_column='RetailPrice', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'snapwithcount'

class Snapshot(models.Model):
    id = models.AutoField(primary_key=True, db_column='AuditId')
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.CharField(db_column='ItemID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sizeid = models.CharField(db_column='SizeID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qtyonhand = models.IntegerField(db_column='QtyOnHand', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.DecimalField(db_column='RetailPrice', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = ' snapshot'

class Auditresultsheader(models.Model):
    auditid = models.IntegerField(db_column='AuditID', primary_key=True)  # Field name made lowercase.
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

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'auditresultsheader'


class Auditresultsline(models.Model):
    id = models.CharField(db_column='id', primary_key=True, max_length=20)  # Field name made lowercase.
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.CharField(db_column='ItemID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sizeid = models.CharField(db_column='SizeID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    countqty = models.IntegerField(db_column='CountQty', blank=True, null=True)  # Field name made lowercase.
    snapqty = models.IntegerField(db_column='SnapQty', blank=True, null=True)  # Field name made lowercase.
    adjustmentqty = models.IntegerField(db_column='AdjustmentQty', blank=True, null=True)  # Field name made lowercase.
    retailprice = models.DecimalField(db_column='RetailPrice', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datareaid = models.CharField(db_column='DatAreaID', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auditresultsline'

class EditcountsqtyVariance(models.Model):
    createdpk = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.CharField(db_column='ItemID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sizeid = models.CharField(db_column='SizeID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=60, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=120, blank=True, null=True)  # Field name made lowercase.
    snapqty = models.IntegerField(db_column='SnapQty', blank=True, null=True)  # Field name made lowercase.
    originalcount = models.IntegerField(db_column='OriginalCount', blank=True, null=True)  # Field name made lowercase.
    currentcount = models.IntegerField(db_column='CurrentCount', blank=True, null=True)  # Field name made lowercase.
    currentvariance = models.IntegerField(db_column='CurrentVariance', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.DecimalField(db_column='RetailPrice', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    accepted = models.BooleanField(db_column='Accepted', blank=True, null=True)  # Field name made lowercase.
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'editcountsqty/variance'


class Editcountbysku(models.Model):
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.CharField(db_column='ItemID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sizeid = models.CharField(db_column='SizeID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=60, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=120, blank=True, null=True)  # Field name made lowercase.
    snapqty = models.IntegerField(db_column='SnapQty', blank=True, null=True)  # Field name made lowercase.
    originalcount = models.IntegerField(db_column='OriginalCount', blank=True, null=True)  # Field name made lowercase.
    currentcount = models.IntegerField(db_column='CurrentCount', blank=True, null=True)  # Field name made lowercase.
    currentvariance = models.IntegerField(db_column='CurrentVariance', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.DecimalField(db_column='RetailPrice', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    accepted = models.BooleanField(db_column='Accepted', blank=True, null=True)  # Field name made lowercase.
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'editcountbysku'

class Departmentlossestimation(models.Model):
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=60, blank=True, null=True)
    unitdifference = models.IntegerField(db_column='UnitDifference', blank=True, null=True)
    lostcost = models.DecimalField(db_column='LostCost', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lostretail = models.DecimalField(db_column='LostRetail', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'departmentlossestimation'

class Lpauditor(models.Model):
    idlpauditor = models.IntegerField(db_column='idLPAuditor', primary_key=True)  # Field name made lowercase.
    staffid = models.IntegerField(db_column='StaffID', blank=True, null=True)  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lpauditor'


class PolicyProcedures(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True, blank=True)  # Field name made lowercase.
    auditid = models.IntegerField(db_column='AuditID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    compliance_level = models.CharField(db_column='ComplianceLevel', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    correctivetext = models.CharField(db_column='CorrectiveText', max_length=45, blank=True, null=True)
    pointvalues = models.IntegerField(db_column='PointValues', blank=True, null=True)
    auditsum = models.IntegerField(db_column='AuditSum', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'policy_procedures'

class PolicyVioloationFacts(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True, blank=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    violoationdescription = models.TextField(db_column='ViolationDescription', blank=True, null=True)  # Field name made lowercase.
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'policyvioloationfacts'

class Productmaster(models.Model):
    categoryid = models.IntegerField(db_column='CategoryID', blank=True, null=True)  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.IntegerField(db_column='TeamID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.CharField(db_column='ItemID', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.CharField(db_column='SizeID', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    descripiton = models.CharField(db_column='Descripiton', max_length=120, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=30, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.DecimalField(db_column='RetailPrice', max_digits=30, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    upc = models.CharField(db_column='UPC', max_length=45, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    sizeorder = models.CharField(db_column='SizeOrder', max_length=12, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    upctypeid = models.IntegerField(db_column='UPCTypeID', blank=True, null=True)  # Field name made lowercase.
    pricechangebefore = models.CharField(db_column='PriceChangeBefore', max_length=45, db_collation='utf8_general_ci', blank=True, null=True)  # Field namemade lowercase.
    pricechangeafter = models.CharField(db_column='PriceChangeAfter', max_length=45, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    discontinue = models.DateTimeField(db_column='Discontinue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productmaster'


class Storeinformation(models.Model):
    storeid = models.IntegerField(db_column='StoreID', primary_key=True)  # Field name made lowercase.
    mallname = models.CharField(db_column='MallName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    hwistoreregionid = models.CharField(db_column='HWIStoreRegionID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    hwistoredistrictid = models.CharField(db_column='HWIStoreDistrictID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lp_region = models.CharField(db_column='LP Region', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    storetypeid = models.CharField(db_column='StoreTypeID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    addtess = models.CharField(db_column='Addtess', max_length=120, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=5, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storeinformation'


class Upcsscanned(models.Model):
    upc = models.CharField(db_column='UPC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    scannedqty = models.IntegerField(db_column='ScannedQty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'upcsscanned'



class UpcsScanned(models.Model):
    # FIXME :: Will just need to go back through and append rest of model fields
    auditID = models.IntegerField()
    storeNumber = models.IntegerField()
    pass