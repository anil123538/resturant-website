from django.shortcuts import render,HttpResponse,redirect
from .models import FoodItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='login')
def index(request):
    return render(request,'index.html',{'username': request.user.username})



def starter(request):
    return render(request,'starter-page.html',{})

   


def register(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        em=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('repeat-password')
        if pass1!=pass2:
            return HttpResponse("Your password and repeat-password are not same")
        else:
            my_user=User.objects.create_user(uname,em,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request,'signup.html',{}) 
    
     
def log(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("email and posswor is incorrect")


    return render(request,'login.html',{})



@login_required(login_url='login')
def order_view(request):
    food_items = FoodItem.objects.filter(available=True)  # Only show available items
    return render(request, 'order.html', {'food_items': food_items})
  
