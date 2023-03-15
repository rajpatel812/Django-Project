from django.db import models

# Create your models here.

class Employee(models.Model):
    username =models.CharField(max_length=50)
    fname =models.CharField(max_length=50)
    lname =models.CharField(max_length=50)
    pincode = models.IntegerField(null=True)
    email =models.EmailField(db_index=True,unique=True,max_length=50)

 