from django.shortcuts import render
from stock.models import Stock



def update_stock(request):
    return render(request, 'stock/update_stock.html')
