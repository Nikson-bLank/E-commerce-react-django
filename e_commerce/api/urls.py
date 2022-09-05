
from django.urls import path,include
from api import views


urlpatterns = [
    path('resume/', views.ProfileView.as_view(), name='resume'),
    path('list/', views.ProfileView.as_view(), name='list'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('productslist/', views.ProductsView.as_view(), name='productlists'),
    path('user_register/',views.user_register,name="user_register"),
    path('check_register/',views.check_register,name="check_register"),
    path('login/',views.login,name="login")
    
  
]
