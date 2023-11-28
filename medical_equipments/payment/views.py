from django.shortcuts import render
from payment.models import Payment
from cart.models import Cart
from product_order.models import ProductOrder
from login.models import Login
from products.models import Product
from django.http import HttpResponseRedirect
import datetime


def seller_view_payments(request):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid,type='seller')
    products = Product.objects.filter(owner_id=owner_id.user_id,product_type='new').values_list('product_id',flat=True)
    cart_ids = Cart.objects.filter(product_id__in=products,cart_status='order placed').values_list('cart_id',flat=True)
    order_ids = ProductOrder.objects.filter(cart_id__in=cart_ids,order_status='accepted').values_list('order_id',flat=True)
    payments = Payment.objects.filter(order_id__in=order_ids)
    context = {
        'details':payments
    }
    return render(request, 'payment/seller_view_payments.html',context)


def subseller_view_payments(request):
    uid = request.session["uid"]
    print("iii",uid)
    owner_id = Login.objects.get(login_id=uid)
    print("pjjjjjj",owner_id)
    print("oooo",owner_id.user_id)
    products = Product.objects.filter(owner_id=owner_id.user_id,product_type='old').values_list('product_id',flat=True)
    cart_ids = Cart.objects.filter(product_id__in=products,cart_status='order placed').values_list('cart_id',flat=True)
    order_ids = ProductOrder.objects.filter(cart_id__in=cart_ids,order_status='accepted').values_list('order_id',flat=True)
    payments = Payment.objects.filter(order_id__in=order_ids)
    context = {
        'details':payments
    }
    return render(request, 'payment/subseller_view_payments.html',context)


def customer_add_payment(request):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid)
    cart_ids = Cart.objects.filter(user_id=owner_id.user_id,cart_status='order placed').values_list('cart_id',flat=True)
    pay_ids = Payment.objects.all().values_list('order_id',flat=True)

    accepted_orders = ProductOrder.objects.filter(cart_id__in=cart_ids,order_status='accepted').exclude(order_id__in=pay_ids)
    context = {
        'data':accepted_orders
    }
    return render(request, 'payment/customer_add_payment.html',context)

def add_payment(request,idd):
    obj = ProductOrder.objects.filter(order_id=idd)
    obb = Payment()
    obb.order_id = idd
    obb.date = datetime.date.today()
    obb.payment_status = 'paid'
    obb.save()
    return HttpResponseRedirect('/payment/customer_add_payment/')


