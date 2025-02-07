from django.forms import ModelForm
from django import forms
from .models import Supplier,Product, StockMovement, SalesOrder

import re

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','email','phone','address']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\d{10}$',phone):
            raise forms.ValidationError('Enter a valid 10-digit phone number.')
        if Supplier.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Supplier with this phone number already exists.")
        return phone
    
    def clean_email(self):
        super().clean()
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
            raise forms.ValidationError('Enter a valid email address.')
        if Supplier.objects.filter(email=email).exists():
            raise forms.ValidationError("Supplier with this email already exists.")
        return email
    
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Product.objects.filter(name=name).exists():
            raise forms.ValidationError("Product with this name already exists.")
        # super().clean()
        return name
    
class StockMovementForm(ModelForm):
    class Meta:
        model = StockMovement
        fields = ['product', 'quantity', 'movement_type', 'notes']

    def clean_quantity(self):
        quantity= self.cleaned_data.get('quantity')
        if not quantity > 0:
            raise forms.ValidationError("Quantity must be greater than 0")
        return quantity
    
class SaleOrderForm(ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['product', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.stock_quantity:
            raise forms.ValidationError("Not enough stock available.")
        return quantity