from django import forms
from .models import Order
from .models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded px-3 py-2 w-full'}),
            'phone': forms.TextInput(attrs={'class': 'border rounded px-3 py-2 w-full'}),
            'address': forms.Textarea(attrs={'class': 'border rounded px-3 py-2 w-full', 'rows':3}),
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'image']   # change based on your model
