from django.shortcuts import render, redirect
from .forms import SupplierForm, ProductForm
from .models import Supplier,Product
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
