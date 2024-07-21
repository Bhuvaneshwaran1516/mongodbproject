from django.db import models


class Stud(models.Model):
    name=models.CharField(max_length=50,null=True)
    age=models.BigIntegerField()
    phone=models.BigIntegerField()
    address=models.CharField(max_length=70,null=True)
    password=models.CharField(max_length=30,null=True)