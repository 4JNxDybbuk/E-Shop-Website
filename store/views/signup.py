from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    # when GET request hit by the url then django automatically called get() method
    def get(self, request):
        return render(request, 'signup.html')

    # when POST request hit by the url then django automatically called post() method
    def post(self, request):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        formsData = {
            'firstName': firstname,
            'lastName': lastname,
            'email': email,
            'phone': phone
        }

        # create customer object..
        customer = Customer(firstname=firstname, lastname=lastname,
                            phone=phone, email=email, password=password)

        # checking signup form validation for customers..
        errorMsg = self.validateCustomer(customer)

        # if form is valid then save data to the database
        if not errorMsg:

            # make_password() method is used for hashing password.
            customer.password = make_password(customer.password)

           # call register() method from customer model and save info to the database.
            customer.register()
            return redirect('/login')
        else:
            data = {
                'errorMsg': errorMsg,
                'formData': formsData,
            }
            return render(request, 'signup.html', data)

    # Cheching Customer Form Validation..
    def validateCustomer(self, customer):
        errorMsg = None
        if not customer.firstname:
            errorMsg = "First Name Is Required !!"
        elif len(customer.firstname) < 5:
            errorMsg = "First Name Must Be 5 Character Long !!"
        elif not customer.lastname:
            errorMsg = "Last Name Is Required !!"
        elif len(customer.phone) < 10:
            errorMsg = "Phone Number Must Be 10 Digit !!"
        elif len(customer.password) < 6:
            errorMsg = "Password Must Be 6 Character Long !!"
        elif not customer.email:
            errorMsg = "Email Id Must Be Required !!"
        elif customer.isEmailExist():
            errorMsg = "Email Already Registered !!"

        return errorMsg
