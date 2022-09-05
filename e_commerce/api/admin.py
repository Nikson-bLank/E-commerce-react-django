from django.contrib import admin
from .models import Product , User, Profile, Products
# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['id','name','email','password','repeat_password']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name','product_price','product_image']

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','dob','state','gender','location','pimage','rdoc']

@admin.register(Products)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','details','price','discount','final_price']


    