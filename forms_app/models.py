from django.db import models

# Create your models here.

class BogieChecksheetForm(models.Model):
    formNumber = models.CharField(max_length=100)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    bogieDetails = models.JSONField()    # stores nested JSON (e.g. bogieNo, dateOfIOH, etc)
    bogieChecksheet = models.JSONField() # stores nested bogie check data
    bmbcChecksheet = models.JSONField()  # stores nested MBBC check data
    status = models.CharField(max_length=50, default='Saved')
    submittedBy = models.CharField(max_length=100, blank=True, null=True)
    submittedDate = models.DateField(blank=True, null=True)

class WheelSpecificationForm(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    fields = models.JSONField()  # JSON of all wheel measurement fields
