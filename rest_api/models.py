from django.db import models

# Create your models here.
class BankData(models.Model):
	ifsc = models.CharField(max_length=250, primary_key=True)
	bank_id = models.IntegerField(null=True, blank=True)
	branch = models.CharField(max_length=250, null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	city = models.CharField(max_length=250, null=True, blank=True)
	district = models.CharField(max_length=250, null=True, blank=True)
	state = models.CharField(max_length=250, null=True, blank=True)
	bank_name = models.CharField(max_length=250, null=True, blank=True)