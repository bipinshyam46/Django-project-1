from django.shortcuts import render,redirect
from .models import *
from .forms import*
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
import random
from datetime import timedelta, date



# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']


        UserData.objects.create_user(name=name,username=username,phone=phone,email=email,password=password)
        return redirect(home)
    
    else:
        return render(request,'signup.html')

def userprofile(request):
    count=0
    id=request.session['user_id']
    user=UserData.objects.get(id=id)
    scoop=Items.objects.filter(item_type='scoop')
    drink=Items.objects.filter(item_type='drinks')
    special=Items.objects.filter(item_type='specialitems')
    return render(request,'userprofile.html',{'scoop':scoop,'drink':drink,'special':special,'user':user,'count':count})

def adminprofile(request):
    return render (request,'adminprofile.html')

def scoops(request):
    items=Items.objects.filter(item_type='scoop')
    return render(request,'scoops.html',{'items':items})

def drinks(request):
    items=Items.objects.filter(item_type='drinks')
    return render(request,'drinks.html',{'items':items})

def specialitems(request):
    items=Items.objects.filter(item_type='specialitems')
    return render(request,'specialitems.html',{'items':items})


def Login(request):
    message=''
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None:
            if user.is_superuser==1:
                login(request,user)
                return redirect(adminprofile)
            
            elif user.is_active==1 and user.is_staff==0:
                login(request,user)
                request.session['user_id']=user.id
                return redirect(userprofile)
            elif user.is_active==1 and user.is_staff==1:
                login(request,user)
                request.session['staff_id']=user.id
                return redirect(staffprofile)
        else:
            message='Invalid Credentials'

            return render(request,'about.html',{'message':message})
    else:
        return render(request,'login.html')

def Logout(request):
    auth.logout(request)
    request.session.flush()
    return redirect(home)

def additem(request):
    if request.method == 'POST':
        form = Itemform(request.POST, request.FILES)
        if form.is_valid():
            item_name=form.cleaned_data.get('item_name')
            price=form.cleaned_data.get('price')
            item_type=form.cleaned_data.get('item_type')
            description=form.cleaned_data.get('description')
            image=form.cleaned_data.get('image')

            new_item=Items.objects.create(
                item_name=item_name,price=price,item_type=item_type,description=description,image=image
            )
            new_item.save()

            return redirect(staffprofile)

    else:
        return render(request,'additem.html')

def viewitem(request):
    items=Items.objects.all()
    return render(request,'viewitem.html',{'items':items})

def edititem(request,id):
    data=Items.objects.get(id=id)
    
    if request.method=='POST':
        form = Itemform(data=request.POST, files=request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect(viewitem)
    else:
        form = Itemform(instance=data)
        return render(request,'edititem.html',{'form':form})

@login_required(login_url='Login')
def order(request,id):
    user_id=request.user.id
    items=Items.objects.filter(id=id)
    for i in items:
        item_id=i.id
    if request.method=='POST':
        item_name=request.POST['item_name']
        quantity=request.POST['quantity']
        total_price=request.POST['total_price']
        payment_mode='COD'
        orders_id='icecream'+str(random.randint(111111,999999))
        while Order.objects.filter(order_id=orders_id) is None:
            orders_id='icecream'+str(random.randint(111111,999999))  
        new_order=Order.objects.create(
                quantity=quantity,total_price=total_price,item_id=item_id,user_id=user_id,order_id=orders_id,item_name=item_name,payment_mode=payment_mode
            )
        # new_order=Order(quantity=quantity,total_price=total_price,user_id=user_id,item_id=item_id)
        # new_order.save()
        return redirect(userprofile)
        

    else:
        return render (request,'order.html',{'items':items})


def staffprofile(request):
    orders=Order.objects.all()
    return render(request,'staffprofile.html',{'orders':orders})

def changestatus(request,id):
    if request.method=='POST':
        # order=Order.objects.filter(id=id)
        status=request.POST['status']
        print("hfhhghsighig=",status)
        # order.status=status
        # order.update()
        Order.objects.filter(id=id).update(status=status)
        return redirect(staffprofile)
    else:
        return render(request,'orderstatus.html')

@login_required(login_url='Login')
def userorder(request):
    user_id=request.user.id
    orders=Order.objects.filter(user_id=user_id)
    return render(request,'userorder.html',{'orders':orders})

def deleteitem(request,id):
    data=Items.objects.get(id=id)
    data.delete()
    return redirect(viewitem)

def schedule_weekly_orders(request, year, week):
    start_date = date.fromisocalendar(year, week, 1)
    end_date = start_date + timedelta(days=6)
    weekly_orders = ScheduleOrder.objects.create()
    context = {'weekly_orders': weekly_orders}
    return render(request, 'schedule_weekly_orders.html', context)