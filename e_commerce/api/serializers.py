from rest_framework import serializers
from .models import Product,User, Profile, Products

# from Logistics.Driver.views import driver_details

class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=100)
    product_price = serializers.IntegerField()
    product_description = serializers.CharField(max_length=100)
    product_stock = serializers.IntegerField()
    product_is_active = serializers.BooleanField()
    product_image = serializers.ImageField(max_length=None,use_url=True)

    def create(self, validate_data):
        return Product.objects.create(**validate_data)

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=75)
    password = serializers.CharField(max_length=12)
    repeat_password = serializers.CharField(max_length=200)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name','email','dob','state','gender','location','pimage','rdoc']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','name','image','details','price','discount','final_price']

