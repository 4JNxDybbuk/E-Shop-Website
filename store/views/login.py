from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View


class Login(View):

    returnURL= None
    # when GET request hit by the url then django automatically called get() method
    def get(self, request):
        # to get return_url value from url.
        Login.returnURL = request.GET.get('return_url')
        return render(request, 'login.html')

    # when POST request hit by the url then django automatically called post() method
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        errorMsg = None
        # get customer details by email..
        customer = Customer.getCustomerByEmail(email)

        if customer:
            # check password hashing
            passwordCheck = check_password(password, customer.password)
            if passwordCheck:
                # creating session after login and store customer id & email to the session variable.
                request.session['customer'] = customer.id
                
                if Login.returnURL:
                    return HttpResponseRedirect(Login.returnURL)
                else:
                    Login.returnURL = None
                    return redirect('/')
            else:
                errorMsg = "Password Does Not Matched !!"
                return render(request, 'login.html', {'errorMsg': errorMsg})

        else:
            errorMsg = "Email Does Not Exists !!"
            return render(request, 'login.html', {'errorMsg': errorMsg})


# Customer logout method, to clear all session variables.
def Logout(request):
    request.session.clear()
    return redirect('/login')