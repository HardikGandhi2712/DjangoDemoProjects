from django.db import models
from django.db.models.deletion import CASCADE
from .models import *
from django.utils.safestring import mark_safe

# Create your models here.

class dept(models.Model):
    dname=models.CharField(max_length=15)
    class Meta:
        db_table="dept"
    def __str__(self):
        return self.dname


class doctor(models.Model):
    doctorname=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    class Meta:
        db_table="doctor"
    def __str__(self):
        return self.doctorname


class item(models.Model):
    itemname=models.CharField(max_length=15)
    price=models.IntegerField()
    category=models.CharField(max_length=10)
    def __str__(self):
        return self.itemname
    class Meta:
        db_table="item"


class itemorder(models.Model):
    customername=models.CharField(max_length=20,default="aaa")
    orderdate=models.DateField()
    quantity=models.IntegerField()
    itemid=models.ForeignKey(item,on_delete=CASCADE)
    def __str__(self):
        return self.customername
    class Meta:
        db_table="itemorder"



class stud(models.Model):
    rno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=20)
    science=models.IntegerField()
    maths=models.IntegerField()
    eng=models.IntegerField()

    def __str__(self):
        return self.sname

    def total(self):
        if self.science and self.maths and self.eng:
            t=self.maths+self.science+self.eng
            return t
        else:
            t=0
            return t

    class Meta:
        db_table='stud'
    



class SDoctor(models.Model):
    qual=[('BDS',"BDS"),('MD',"MD"),('MBBS',"MBBS")]
    dname=models.CharField(max_length=20)
    qual=models.CharField(max_length=5,choices=qual)
    
    def __str__(self):
        return self.dname
    
    class Meta:
        db_table="vdoctor"



class Car(models.Model):
    cno=models.AutoField(primary_key=True)
    carname=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    price=models.IntegerField()
    pic=models.ImageField()
    
    def __str__(self):
        return self.carname
    
    class Meta:
        db_table="car"

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.pic.url))
    image_tag.short_description='image'