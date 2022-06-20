from cgi import print_exception
from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from django.db import models
from matplotlib import image
from datetime import datetime
import random

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=TRUE)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    pub_year = models.IntegerField()
    product_category = models.CharField(max_length=50, default="")
    product_subcategory = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="shop/images", default="")
    price= models.IntegerField(default=0)
    status= models.CharField(max_length=50, default="")
    brand = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    my_order_id=models.CharField(max_length=50,default="unavailable")
    items = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip_code = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.my_order_id
    


