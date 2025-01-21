from django.urls import path
from . import views

urlpatterns = [
    path('supplier/add/', views.AddSupplier,name='add_supplier'),
    path('supplier/list/',views.SupplierList,name='supplier_list'),

    path('product/add/', views.AddProduct , name='add_product'),
    path('product/list/', views.ProductList , name='product_list'),

    path('stock_movement/',views.AddStockMovement, name='stock_movement'),
    path('stock_level/', views.CheckStockLevel , name='stock_level'),

    path('sale_order/create/', views.CreateSaleOrder , name='create-sale-order'),
    path('sale_order/list/',views.ListOfSaleOrders , name='sale_order_list'),
]
