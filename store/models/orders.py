from tkinter import CASCADE
from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete= models.CASCADE)
    quantity = models.IntegerField(default= 1)
    price = models.IntegerField()
    address = models.CharField(max_length= 150 , default= '')
    phone = models.CharField(max_length= 50 , default= '')
    date = models.DateField(default= datetime.datetime.today)
    status = models.BooleanField(default=False)


    # to save customer ordewho i9s currently login
    def placeOrder(self):
        self.save()


    @staticmethod
    def getOrderByCustomer(customerID):
        return Order.objects.filter(customer = customerID)