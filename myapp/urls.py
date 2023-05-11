from myapp import views
from django.urls import path
from .views import *


urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('staffsignup',views.staffsignup,name='staffsignup'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('adminprofile',views.adminprofile,name='adminprofile'),
    path('staffprofile',views.staffprofile,name='staffprofile'),
    path('scoops',views.scoops,name='scoops'),
    path('drinks',views.drinks,name='drinks'),
    path('specialitems',views.specialitems,name='specialitems'),
    path('additem',views.additem,name='additem'),
    path('viewitem',views.viewitem,name='viewitem'),
    path('deleteitem/<int:id>',views.deleteitem,name='deleteitem'),
    path('edititem/<int:id>',views.edititem,name='edititem'),
    path('order/<int:id>',views.order,name='order'),
    path('changestatus/<int:id>',views.changestatus,name='changestatus'),
    path('userorder',views.userorder,name='userorder'),
    path('schedule',views.schedule_order,name='schedule'),

    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),


]