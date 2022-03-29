
from django.urls import path
from .views import index , login , signup ,cart
from .middlewares.auth import authMiddleware

urlpatterns = [
    path('' , index.Index.as_view()),
    # path('category/<categoryID>' , productByCategory)
    path('signup' , signup.Signup.as_view()),
    path('login' ,  login.Login.as_view()),
    path('logout' , login.Logout),
    # to add custom middleware to check whther the user is logged in or not.
    path('cart' , authMiddleware(cart.Cart.as_view()) ),
    path('checkout' , cart.Checkout.as_view()),
    # to add custom middleware to check whther the user is logged in or not.
    path('orders/' , authMiddleware(cart.OrderView.as_view()) ),
]
