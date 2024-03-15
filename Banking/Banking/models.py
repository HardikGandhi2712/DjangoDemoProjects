from django.db import models
from .models import *

class account(models.Model):
    accno=models.IntegerField()
    pin=models.IntegerField()
    custname=models.CharField(max_length=25)
    balance=models.IntegerField()

    class Meta:
        db_table="account"

    def __str__(self):
        return self.custname
        

class acctrans(models.Model):
    txdate=models.DateField()
    accno=models.IntegerField()
    txtype=models.CharField(max_length=15)
    amount=models.IntegerField()
    class Meta:
        db_table="acctrans"
    def __str__(self):
        return self.txtype