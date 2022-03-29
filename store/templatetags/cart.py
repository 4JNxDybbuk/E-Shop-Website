
from django import template

register = template.Library()


# to check the specific product present in cart or not ..
@register.filter(name="is_in_cart")
def is_in_cart(product , cart):
    # to get all keys from cart dictionary.
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


# to return cart quantity of specific product with respect to product id
@register.filter(name="cart_quantity")
def cart_quantity(product , cart):
    # to get all keys from cart dictionary.
    keys = cart.keys()
    for item in keys:
        if int(item) == product.id:
            return cart.get(item)
    return 0


# to return total amount for the specific product.
@register.filter(name="totalProduct")
def totalProduct(product , cart):
    # to get all keys from cart dictionary.
    keys = cart.keys()
    for item in keys:
        if int(item) == product.id:
            return cart.get(item) * product.price
    return 0



# to return the grand total of all products.
@register.filter(name="totalCartPrice")
def totalCartPrice(products , cart):
    sum = 0
    for product in products:
        sum += totalProduct(product , cart)
    
    return sum




@register.filter(name="orderPrice")
def orderPrice(quantity , price):  
    return quantity * price