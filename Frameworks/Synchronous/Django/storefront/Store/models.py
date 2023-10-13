from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("Product Name", max_length=256)
    description = models.TextField("Product Description", max_length=1024)
    quantity = models.IntegerField("Quantity")
    price = models.DecimalField("Price")

class Cart(models.Model):
    time_created = models.DateTimeField("Time Created")
    cart_items = models.ManyToManyField(Product)
