from django.db import models

class menu(models.Model):
    menuname=models.CharField(max_length=25)
    category=models.CharField(max_length=25)
    photo=models.ImageField()
    rate=models.IntegerField()
    class Meta:
        db_table="menu"