from django.db import models
from django.forms import ModelForm

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class UploadFile(models.Model):
    # Uploads it to MEDIA_ROOT/uploads/
    files = models.FileField(
        upload_to='uploads/',
        blank=True,
        null=True
    )


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

#class SnapReportForm(ModelForm):
 #   class Meta:
  #      model = Snapshot
   #     fields = ['AuditID', 'StoreID', 'ItemID', 'SizeID', 'QtyOnHand', 'Cost', 'RetailPrice']

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
    createdtransactionid = models.CharField(db_column='CreatedTransactionID', primary_key=True, max_length=20)  # Field name made lowercase.
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
    createdpk = models.IntegerField(db_column='CreatedPK', primary_key=True)  # Field name made lowercase.
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
    fieldname = models.CharField(db_column='FieldName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    compliance_level = models.IntegerField(db_column='ComplianceLevel', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'policy_procedures'


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

class uploadFileTestModel(models.Model):
    file = models.FileField(
        upload_to='upload/',
        blank=True,
        null=True
    )