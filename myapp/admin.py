from django.contrib import admin

# Register your models here
from .models import UserData,Items

admin.site.register(UserData)
admin.site.register(Items)

