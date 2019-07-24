from django.db import models

class Customer_details(models.Model):
    USERNAME = models.CharField(max_length=150)
    PASSWORD = models.CharField(max_length=150)
    EMAIL = models.EmailField(primary_key=True, max_length=150)
    MOBILENO = models.CharField(max_length=10)
    OTP=models.CharField(max_length=50,default=True)


class Vendor_details(models.Model):
    USERNAME = models.CharField(max_length=150)
    PASSWORD = models.CharField(max_length=150)
    EMAIL = models.EmailField(primary_key=True, max_length=150)
    MOBILENO = models.CharField(max_length=10)
    OTP=models.CharField(max_length=50)

class Add_newproduct(models.Model):
    TYPE = models.CharField(max_length=50)
    CATEGORIES = models.CharField(max_length= 50)
    CATEGORIETYPE = models.CharField(max_length= 50)
    SIZE = models.CharField(max_length=20)
    QUANTITY = models.CharField(max_length= 50)
    NAME = models.CharField(max_length= 100)
    IMAGE = models.ImageField(upload_to="my_images",default=False)
    PRICE = models.DecimalField(max_digits=10,decimal_places=2)
    DESCRIPTION = models.CharField(max_length=500)

