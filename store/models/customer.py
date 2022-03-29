from statistics import mode
from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length= 50)
    lastname = models.CharField(max_length= 50)
    phone = models.CharField(max_length= 50)
    email = models.EmailField()
    password = models.CharField(max_length= 250)


    #to register customer and save the customer details into the database.
    def register(self):
        self.save()


    #Checking for Email existing 
    def isEmailExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
    

    # this method for customer login.
    @staticmethod
    def getCustomerByEmail(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False
