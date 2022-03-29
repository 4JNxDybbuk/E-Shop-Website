from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from store.models.product import Product
from store.models.Category import Ctaegory
from django.views import View


class Index(View):

    # when GET request hit by the url then django automatically called get() method
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        categories = Ctaegory.get_all_category()
        categoryID = request.GET.get('category')

        if categoryID:
            products = Product.get_products_by_category(categoryID)
        else:
            products = Product.get_all_products()
        data = {
            'products': products,
            'categories': categories
        }
        # print(products)
        # print the session variables value to check customer is login or not.
        # print("You Are = "  , request.session.get('customerEmail'))

        return render(request, 'index.html', data)

    # when POST request hit by the url then django automatically called post() method

    def post(self, request):
        productID = request.POST.get('productID')
        removeProduct = request.POST.get('removeProduct')

        # to get session cart variable value ..
        cart = request.session.get('cart')
        if cart:
            # to check product quantity, if quantity exist  increment by 1 then add to cart
            quantity = cart.get(productID)
            if quantity:
                if removeProduct:
                    if quantity <= 1:
                        cart.pop(productID)
                    else:
                        cart[productID] = quantity - 1
                else:
                    cart[productID] = quantity + 1
            else:
                cart[productID] = 1
        else:
            cart = {}
            cart[productID] = 1

        # set session cart and store cart dictionary into session
        request.session['cart'] = cart
        # print(request.session['cart'])
        return redirect('/')
