from collections.abc import Iterable
from django.db import models
import datetime
from django.db.models.query import QuerySet
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField("Product Name", max_length=256)
    description = models.TextField("Product Description", max_length=1024)
    quantity = models.IntegerField("Quantity")
    price = models.DecimalField(decimal_places=2, max_digits=6)
    product_department = models.ForeignKey("Department", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Department(models.Model):
    department_name = models.CharField(max_length=64)
    product_highlight = models.OneToOneField(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self) -> str:
        return self.department_name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    family_name = models.CharField(max_length=32)
    customer_cart = models.OneToOneField("Cart", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return " ".join([self.first_name, self.family_name]) 

class MyCartManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(last_modified__lt=timezone.now() - datetime.timedelta(minutes=30))

class Cart(models.Model):
    last_modified = models.DateTimeField(default=timezone.now, editable=False)
    cart_items = models.ManyToManyField(Product)
    cart_customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True)
    objects = models.Manager()
    old_carts = MyCartManager()

    def save(self):
        self.last_modified = timezone.now()
        return super().save()

    def __str__(self) -> str:
        name = self.cart_customer.first_name if self.cart_customer else "Nobody"

        return name + "'s Cart"

    def is_an_old_cart(self):
        return self.last_modified <= timezone.now() - datetime.timedelta(minutes=30)

class Order(models.Model):
    time_created = models.DateTimeField("Time Created", editable=False)
    order_items = models.ManyToManyField(Product)
    order_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Order Number: {self.id}"
