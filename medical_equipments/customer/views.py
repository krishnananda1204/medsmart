from django.shortcuts import render
from customer.models import Customer
from login.models import Login
from seller.models import Seller
from subseller.models import *


def registration(request):
    if request.method == 'POST' and 'reg' in request.POST:
        obj=Customer()
        obj.name = request.POST.get('name')
        obj.address = request.POST.get('address')
        obj.phone = request.POST.get('phone')
        obj.email = request.POST.get('email')
        obj.save()

        obb=Login()
        obb.username = request.POST.get('email')
        obb.password = request.POST.get('password')
        obb.user_id = obj.customer_id
        obb.type = 'customer'
        obb.save()
    
    if request.method == 'POST' and 'subsellerreg' in request.POST:
        obj=Subseller()
        obj.name = request.POST.get('subsellername')
        obj.address = request.POST.get('subselleraddress')
        obj.phone = request.POST.get('subsellerphone')
        obj.email = request.POST.get('subselleremail')
        obj.save()

        obb=Login()
        obb.username = request.POST.get('subselleremail')
        obb.password = request.POST.get('subsellerpassword')
        obb.user_id = obj.subseller_id
        obb.type = 'subseller'
        obb.save()
    
    if request.method == 'POST' and 'sellerreg' in request.POST:
        obj=Seller()
        obj.name = request.POST.get('sellername')
        obj.address = request.POST.get('selleraddress')
        obj.phone = request.POST.get('sellerphone')
        obj.email = request.POST.get('selleremail')
        obj.save()

        obb=Login()
        obb.username = request.POST.get('selleremail')
        obb.password = request.POST.get('sellerpassword')
        obb.user_id = obj.seller_id
        obb.type = 'seller'
        obb.save()
    return render(request, 'customer/registration.html')



def customer_home(request):
    return render(request, 'customer/customer_home.html')
