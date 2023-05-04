from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserData(AbstractUser):
    name=models.CharField(max_length=100,blank=False,verbose_name='Name')
    phone=models.IntegerField(blank=False,verbose_name='Phone number')
    class Meta:
        db_table='Usertable'

class Items(models.Model):
    item_name=models.CharField(max_length=100,blank=False,verbose_name="Item")
    price=models.IntegerField(blank=False,verbose_name='Price')
    item_type=models.CharField(max_length=100,blank=False,verbose_name='Type')
    description=models.CharField(max_length=300,blank=False,verbose_name="Description")
    image=models.ImageField(upload_to = 'img')

class Order(models.Model):
    user=models.ForeignKey(UserData,on_delete=models.CASCADE)
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    item_name=models.TextField(null=True,verbose_name='Item name')
    quantity=models.IntegerField(blank=False,verbose_name='Quantity')
    token=models.IntegerField(null=True,verbose_name='Token')
    order_date=models.DateField(auto_now_add=True)
    order_id=models.CharField(max_length=200,null=True,verbose_name='Order id')
    payment_mode=models.CharField(max_length=200,null=True,verbose_name='Payment mode')
    payment_id=models.CharField(max_length=200,null=True,verbose_name='Payment id')
    order_status=(
        ('pending','pending'),
        ('accepted','accepted'),
        ('out for delivery','out for delivery'),
        ('completed','completed')
    )
    status=models.CharField(max_length=150,choices=order_status,default='pending',verbose_name='Order status')
    total_price=models.FloatField(null=False,verbose_name='Total price')


class ScheduleOrder(models.Model):
    user=models.ForeignKey(UserData,on_delete=models.CASCADE)
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    day_1=models.TextField(null=True,verbose_name='Day 1')
    day_2=models.TextField(null=True,verbose_name='Day 2')
    day_3=models.TextField(null=True,verbose_name='Day 3')
    day_4=models.TextField(null=True,verbose_name='Day 4')
    day_5=models.TextField(null=True,verbose_name='Day 5')
    day_6=models.TextField(null=True,verbose_name='Day 6')
    day_7=models.TextField(null=True,verbose_name='Day 7')
    quantity=models.IntegerField(blank=False,verbose_name='Quantity')
    token=models.IntegerField(null=True,verbose_name='Token')
    start_date=models.DateField(blank=False)
    end_date=models.DateField(blank=False)
    order_id=models.CharField(max_length=200,null=True,verbose_name='Order id')
    payment_mode=models.CharField(max_length=200,null=True,verbose_name='Payment mode')
    payment_id=models.CharField(max_length=200,null=True,verbose_name='Payment id')
    order_status=(
        ('pending','pending'),
        ('accepted','accepted'),
        ('out for delivery','out for delivery'),
        ('completed','completed')
    )
    status=models.CharField(max_length=150,choices=order_status,default='pending',verbose_name='Order status')
    actual_totalprice=models.FloatField(null=False,verbose_name='Actual total price')
    offer=models.FloatField(null=False,verbose_name='offer')
    total_price=models.FloatField(null=False,verbose_name='Total price')