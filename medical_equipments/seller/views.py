from django.shortcuts import render
from seller.models import Seller


def seller_home(request):
    return render(request, 'seller/seller_home.html')
