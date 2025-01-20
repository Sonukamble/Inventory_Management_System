from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=3,
                                     choices=[("In", "InComing"), ("Out", "OutGoing")]
    )
    movement_date=models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return f"{self.movement_type} - {self.product.name}"