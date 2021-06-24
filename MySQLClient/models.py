from django.db import models


# Create your models here.
class testM(models.Model):
    testID = models.IntegerField(primary_key=True)
    storeName = models.CharField(
        max_length=25
    )
    date= models.DateField()
    itemID = models.CharField(
        max_length=30
    )
    variance = models.SmallIntegerField()
class testForeignKeyM(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    test = models.ForeignKey(testM, on_delete=models.CASCADE)
