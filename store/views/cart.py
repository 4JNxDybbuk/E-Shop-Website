from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
from store.models.orders import Order
from django.views import View


class Cart(View):

    # when GET request hit by the url then django automatically called get() method
    def get(self, request):
        # print(list(request.session.get('cart').keys()))
        # coverting Dictionary to List
        productIds = list(request.session.get('cart').keys())
        # call Product static method from product models.
        getProducts = Product.getProductByID(productIds)
        # print(getProducts)
        return render(request, 'cart.html', {'productCart': getProducts})


# Customer checkout
class Checkout(View):
    # when POST request hit by the url then django automatically called get() method
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        # to get customer id who is currently login using session variable.
        customer = request.session.get('customer')
        # to get cart dictionary value using session cart variable
        cart = request.session.get('cart')
        # to get all product ids from db which is store in the cart dictionary..
        products = Product.getProductByID(list(cart.keys()))
        # print(address , phone , customer , products)

        for product in products:
            order = Order(product=product,
                          customer=Customer(id=customer),
                          quantity=cart.get(str(product.id)),
                          price=product.price,
                          address=address,
                          phone=phone)
            order.placeOrder()
        # after customer checkout the cart should be empty
        request.session['cart'] = {}

        return redirect('/cart')


class OrderView(View):
    # when GET request hit by the url then django automatically called get() method

    def get(self, request):
        # to get customer id who is currently login using session variable.
        customer = request.session.get('customer')
        orders = Order.getOrderByCustomer(customer)
        # print(orders)
        return render(request, 'orders.html', {'orders': orders})
