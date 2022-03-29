from unicodedata import category
from  django.db import models
from .Category import Ctaegory

class Product(models.Model):
    name = models.CharField(max_length= 50)
    price = models.IntegerField(default= 0)
    category = models.ForeignKey(Ctaegory , on_delete= models.CASCADE , default= 1)
    description = models.CharField(max_length= 200 , default= '')
    image = models.ImageField(upload_to ='uploads/products/')


    #get all products from database.
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    #get product by category.
    @staticmethod
    def get_products_by_category(categoryID):
        if categoryID:
            return Product.objects.filter(category = categoryID)
        else:
            return Product.get_all_products()


    # to get product lists from database, id__in returns the all productid     
    @staticmethod
    def getProductByID(productIds):
        return Product.objects.filter(id__in = productIds)