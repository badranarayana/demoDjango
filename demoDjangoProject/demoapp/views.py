from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .models import Customer
from datetime import datetime

# Create your views here.

def index(request):
    # business logic
    # retrieve data from db
    # render html temlate with data
    return HttpResponse("This is my demo app view result")


def create_contact(request):
    if request.method == 'GET': #method attribute is used to identify http method request
        return render(request, 'demoapp/contact.html') # html

    elif request.method == 'POST':
        """
        (Pdb) request.POST
<QueryDict: {'csrfmiddlewaretoken': ['7q8Rn1NrRbOm10fk53EL3Zd8FHVNN5FUlH7beqoYm4Ipr2AibzQLOGViIIOw4ByM'], 'name': ['srinu'], 'phone': ['
+9102020233'], 'location': ['hyderabad'], 'email': ['test@123.com'], 'pin_code': ['436722'], 'dob': ['1991-01-23']}>
        """
        #import pdb;pdb.set_trace()
        # name, phone, location, email. pin code, birth data
        name = request.POST['name']
        phone= request.POST['phone']
        location = request.POST['location']
        email = request.POST['email']
        pin_code = request.POST['pin_code']
        birth_date = request.POST['dob']
        # insert into db
        my_contact = Contact(name=name, phone=phone, location=location,
                         email=email, pin_code=pin_code, birth_date=birth_date)
        # apply changes to db
        my_contact.save()

    # we read data from request(input data from user) and store into database with model class
    return HttpResponse("Contact saved successfully..")


def contact_list(request):
    # db
    # get the contacts from db
    # with model
    contacts_query_set = Contact.objects.all()
    context = {
        'contacts': contacts_query_set
    }
    return render(request, 'demoapp/list_contacts.html', context=context)



#  customer views
def create_customer(request):
    # get request , need to display html page
    # post data and save to db

    if request.method == 'GET':
        return render(request, 'demoapp/createCustomer.html', context={})
    elif request.method == 'POST':
        name = request.POST['name']
        mobile_number = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        pin_code = request.POST['pin_code']

        # lets save into db
        obj = Customer(name=name, mobile_number=mobile_number,
                       address=address, pin_code=pin_code)

        obj.save()

        return HttpResponse("Customer saved successfully")


def list_customers(request):
    # get the customer data
    customers = Customer.objects.all()
    #
    return render(request, 'demoapp/customerList.html', context={
        'customers': customers,
        'current_date': datetime.now(), # format here and pass to context #
        'name': "badra alavala"
    })






