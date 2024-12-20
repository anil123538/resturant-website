from django.shortcuts import render,HttpResponse,redirect
from .models import FoodItem,Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
# Create your views here.



@login_required(login_url='login')
def index(request):
    return render(request,'index.html',{'username': request.user.username})



def starter(request):
    return render(request,'starter-page.html',{})

   
# views.py


@login_required
def bill_view(request, food_id):
    food_item = FoodItem.objects.get(id=food_id)
    
    # Ensure service_charge is a Decimal
    service_charge = Decimal('5.00')  # Use a Decimal value for the service charge
    total_amount = food_item.price + service_charge  # Both are now Decimal, so this will work

    if request.method == 'POST':
        address = request.POST.get('address')
        if address:
            # Create order
            order = Order.objects.create(
                user=request.user,
                food_item=food_item,
                address=address,
                total_amount=total_amount,
                service_charge=service_charge
            )
            order.save()
            messages.success(request, "Your order has been placed successfully!")
            return redirect('index')  # Redirect to the home page or another view
        else:
            messages.error(request, "Please provide an address.",)

    return render(request, 'bill.html',
        { 'username': request.user.username,
        'food_item': food_item,
        'total_amount': total_amount,
        'service_charge': service_charge,
    })


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
    return render(request, 'order.html', {'food_items': food_items, 'username': request.user.username})

  
