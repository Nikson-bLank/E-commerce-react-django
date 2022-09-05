from http.client import HTTPResponse
import json
from django.shortcuts import render ,redirect
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .models import Product , User
from rest_framework.response import Response
from .models import Profile, Products
from .serializers import ProfileSerializer,ProductsSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
def home(request):
    imagess= Products.objects.all()
    img = []
    for images in imagess:
        img.append(images.image)
    print("--------------",img)
    return render(request,'index.html',{'img':imagess})

def shop_details(request):
    return render(request, 'details.html')

def search(request):
    if request.method=="POST":
        name = request.POST.get('name')
        print("name",name)
        print(type(name))
        srch = Products.objects.filter(name=name)
        print("=============",len(srch))
        if len(srch) <= 0:
            print("hhhhhhhhhhhhhhhhf ekvd,sssss")
            return render(request,'no_data_found.html')
        else:
            data = []
            for srh in srch:
                data.append(srh)

            print(srch)
            return render(request,'details.html',{'img':data})
    return HttpResponse(request,'index.html')

def user_register(request):
    return render(request,'register.html')

def check_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if password == repeat_password:
            data = User(name = name, email = email, password=password, repeat_password=repeat_password)
            print("data",data)
            data.save()
            return render(request ,'login.html')
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        check = User.objects.filter(email=email).first()
        if check:
            return redirect('/')
        return redirect('/api/login/')
    return render(request,'login.html')


@csrf_exempt
def product_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ProductSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            # return JsonResponse(json_data)
            return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')

def product_detail(request):
    # user_id = request.session.get('user_id')
    dr = Product.objects.all()
    # file_decode = base64.b64decode(dr.product_image)
    serializers = ProductSerializer(dr, many = True)
    # print(serializers.data)
    # print("ss",serializers)
    json_data = JSONRenderer().render(serializers.data)
    # print("json_data",json_data)
    return HttpResponse(json_data,content_type= 'application/json')
    # return render (request,'profile.html',{'serializers':serializers.data} )

class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Resume Uploaded Successfully',
                            'status':'success', 'candidate':serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        candidate  = Profile.objects.all()
        serializer = ProfileSerializer(candidate, many=True)
        return Response({'status':'success', 'candidates':serializer.data}, status=status.HTTP_200_OK)


class ProductsView(APIView):
    def post(self, request, format=None):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Product Uploaded Successfully',
                            'status':'success','prodct':serializer.data},
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self, request, format=None):
        prodct = Products.objects.all()
        serializer = ProductsSerializer(prodct, many=True)
        return Response({'status':'success', 'prodct':serializer.data}, status=status.HTTP_200_OK)
