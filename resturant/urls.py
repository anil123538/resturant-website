from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from resturant import views

urlpatterns = [
    
     path('/home', views.index,name='index'),
     path('login/',views.log,name='login'),
     
     path('',views.register,name='signup'),
     path('order/', views.order_view, name='order'),
     path('order/<int:food_id>/', views.bill_view, name='bill'),

]