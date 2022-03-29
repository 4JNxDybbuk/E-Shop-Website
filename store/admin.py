from django.contrib import admin
from .models.product import Product
from .models.Category import Ctaegory
from .models.customer import Customer
from .models.orders import Order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price', 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstname' , 'lastname' , 'phone' , 'email' , 'password']


admin.site.register(Product , ProductAdmin)
admin.site.register(Ctaegory , CategoryAdmin)
admin.site.register(Customer , CustomerAdmin)
admin.site.register(Order)