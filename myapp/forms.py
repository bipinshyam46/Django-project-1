from django import forms
from .models import *

class Itemform(forms.ModelForm):
    class Meta:
        model=Items
        fields="__all__"
        # widgets={
        #     'item_name': forms.TextInput(attrs={
        #         'class': 'form-control border-0 p-4'
        #     }),
        #     'type': forms.TextInput(attrs={
        #         'class': 'form-control border-0 p-4'
        #     }),
        #     'price': forms.TextInput(attrs={
        #         'class': 'form-control border-0 p-4'
        #     }),
        #     'description': forms.TextInput(attrs={
        #         'class': 'form-control border-0 p-4'
        #     }),
        #     'image': forms.TextInput(attrs={
        #         'class': 'form-control border-0 p-4'
        #     }),
        # }

class orderform(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"