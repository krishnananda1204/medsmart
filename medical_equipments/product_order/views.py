from django.shortcuts import render
from product_order.models import ProductOrder
from products.models import Product
from complaints.models import Complaint
from login.models import Login
from cart.models import Cart
from stock.models import Stock
from django.http import HttpResponseRedirect
from payment.models import Payment


def customer_manage_order(request):
    uid = request.session["uid"]
    obj=ProductOrder.objects.filter(user_id=uid)
    print(obj)
    context = {
        'details' : obj
    }
    return render(request, 'product_order/customer_manage_order.html',context)


def seller_manage_order(request):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid,type='seller')
    product_ids = Product.objects.filter(product_type='new',owner_id=owner_id.user_id).values_list('product_id',flat=True)
    cart_ids = Cart.objects.filter(product_id__in=product_ids,cart_status='order placed')
    obj = ProductOrder.objects.filter(order_status='pending',cart_id__in=cart_ids)

    stocks = Stock.objects.filter(product_id__in=product_ids)
    context = {
        'details':obj,
        'stocks':stocks
    }
    return render(request, 'product_order/seller_manage_order.html',context)


def subseller_manage_order(request):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid,type='subseller')
    product_ids = Product.objects.filter(product_type='old',owner_id=owner_id.user_id).values_list('product_id',flat=True)
    cart_ids = Cart.objects.filter(product_id__in=product_ids,cart_status='order placed')
    obj = ProductOrder.objects.filter(order_status='pending',cart_id__in=cart_ids)

    stocks = Stock.objects.filter(product_id__in=product_ids)
    context = {
        'details':obj,
        'stocks':stocks
    }
    return render(request, 'product_order/subseller_manage_order.html',context)

def subseller_accept_order(request,idd):
    obj = ProductOrder.objects.get(order_id=idd)
    obj.order_status = 'accepted'
    obj.save()
    return HttpResponseRedirect('/product_order/subseller_manage_order/')

def subseller_reject_order(request,idd):
    obj = ProductOrder.objects.get(order_id=idd)
    obj.order_status = 'rejected'
    obj.save()
    return HttpResponseRedirect('/product_order/subseller_manage_order/')


def seller_accept_order(request,idd):
    obj = ProductOrder.objects.get(order_id=idd)
    obj.order_status = 'accepted'
    obj.save()
    return HttpResponseRedirect('/product_order/seller_manage_order/')

def seller_reject_order(request,idd):
    obj = ProductOrder.objects.get(order_id=idd)
    obj.order_status = 'rejected'
    obj.save()
    return HttpResponseRedirect('/product_order/seller_manage_order/')

def customer_view_order_history(request):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid)
    order_ids = ProductOrder.objects.filter(user_id=owner_id.user_id,order_status='accepted').values_list('order_id',flat=True)
    payments = Payment.objects.filter(order_id__in=order_ids)

    complaints = Complaint.objects.filter(user_id=owner_id.user_id)
    print("==========",complaints)
    context = {
        'details':payments,
        'complaints':complaints
    }
    return render(request,'product_order/customer_view_order_history.html',context)