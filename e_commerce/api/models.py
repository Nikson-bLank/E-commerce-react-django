from audioop import maxpp
from decimal import MAX_EMAX
from distutils.command.upload import upload
from lib2to3.refactor import get_fixers_from_package
from tkinter import CASCADE
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=12)
    repeat_password = models.CharField(max_length=200)

class Product(models.Model):
    # product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100)
    product_stock = models.IntegerField()
    product_is_active = models.BooleanField()
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='Product_images/',blank=True, null=True)



STATE_CHOICE = ((
    ('madhya pradesh','madhya pradesh'),
    ('bihar','bihar'),
    ('gujrat','gujrat')
 ))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='pimage', blank=True)
    rdoc = models.FileField(upload_to='rdocs', blank=True)

class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='productsimage', blank=True)
    details = models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.IntegerField()
    final_price = models.IntegerField()

class Model(models.Model):
    model_name = models.CharField(max_length=100)

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

class Category(models.Model):
    # name = models.ForeignKey('Products',related_name='name', blank=True, null=True, on_delete=models.PROTECT, verbose_name=("name"))
    name = models.ForeignKey(
        'Products',
        on_delete=models.CASCADE,
    )
    






