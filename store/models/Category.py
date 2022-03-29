from unicodedata import name
from django.db import models

class Ctaegory(models.Model):
    name = models.CharField(max_length= 30)

    # to return string.
    def __str__(self):
        return self.name

    #get all category from database
    @staticmethod
    def get_all_category():
        return Ctaegory.objects.all()
    