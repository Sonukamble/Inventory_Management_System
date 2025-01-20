from django.urls import path
from . import views

urlpatterns = [
    path('supplier/add/', views.AddSupplier,name='add_supplier'),
    path('supplier/list/',views.SupplierList,name='supplier_list'),

    path('product/add/', views.AddProduct , name='add_product'),
    path('product/list/', views.ProductList , name='product_list'),
]
