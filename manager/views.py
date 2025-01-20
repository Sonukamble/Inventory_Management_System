from django.shortcuts import render, redirect
from .forms import SupplierForm, ProductForm, StockMovementForm
from .models import Supplier,Product, StockMovement

from decimal import Decimal
from bson import Decimal128
# Create your views here.

def AddSupplier(request):
    if request.method=='POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
        else:
            return render(request,'supplier/add.html',{'form':form})

    form =SupplierForm()
    return render(request,'supplier/add.html',{'form':form})

def SupplierList(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier/list.html',{'suppliers':suppliers})


def AddProduct(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            return render(request,'products/add.html',{'form':form})
    form =ProductForm()
    return render(request,'products/add.html',{'form':form})

def ProductList(request):
    products = Product.objects.all()
    return render(request,'products/list.html',{'products':products})


def AddStockMovement(request):
    if request.method == 'POST':
        form = StockMovementForm(request.POST)
        if form.is_valid():
            stock_movement=form.save(commit=False)
            # Convert Decimal128 to Decimal if the price is in Decimal128 format
            if isinstance(stock_movement.product.price, Decimal128):
                stock_movement.product.price = stock_movement.product.price.to_decimal()

            # Ensure price is a valid Decimal type
            stock_movement.product.price = Decimal(stock_movement.product.price)
            
            if stock_movement.movement_type =='In':
                stock_movement.product.stock_quantity += stock_movement.quantity
            if stock_movement.movement_type == 'Out':
                stock_movement.product.stock_quantity -= stock_movement.quantity

            stock_movement.product.save()
            stock_movement.save()
            return redirect('product_list')
        else:
            return render(request, 'stock_movement.html', {'form':form})

    form = StockMovementForm()
    return render(request, 'stock_movement.html', {'form':form})

def CheckStockLevel(request):
    products= Product.objects.all()

    product_stock_info=[]
    for product in products:
        product_stock_info.append({
            'name': product.name,
            'stock_quantity': product.stock_quantity,
            'category': product.category,
            'price': product.price,
            'supplier': product.supplier.name if product.supplier else "No Supplier"
        })
    return render(request,'stock_level.html',{'product_stock_info': product_stock_info})