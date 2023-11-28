from django.shortcuts import render
from complaints.models import Complaint
import datetime
from payment.models import Payment
from cart.models import Cart
from product_order.models import ProductOrder
from complaints.models import Complaint
from products.models import Product
from login.models import Login

def customer_post_complaint(request,idd):
    payment_id = Payment.objects.get(payment_id = idd)
    order_id = ProductOrder.objects.get(order_id=payment_id.order_id)
    cart_id = Cart.objects.get(cart_id=order_id.cart_id)
    product_id = Product.objects.get(product_id=cart_id.product_id)
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid)
    if request.method == 'POST':
        complaint = request.POST.get('complaint')
        obj = Complaint()
        obj.complaint = complaint
        obj.reply = 'pending'
        obj.date = datetime.date.today()
        obj.user_id = owner_id.user_id
        obj.owner_id = product_id.owner_id
        obj.product_type = product_id.product_type
        obj.save()
    return render(request,
     'complaints/customer_post_complaint.html')

def customer_view_reply(request):
    return render(request, 'complaint/customer_view_reply.html')

def seller_post_reply(request,idd):
    if request.method == 'POST':
        reply = request.POST.get('reply')
        obj = Complaint.objects.get(complaint_id=idd)
        obj.reply = reply 
        obj.save()
    return render(request, 'complaints/seller_post_reply.html')

def subseller_post_reply(request,idd):
    if request.method == 'POST':
        reply = request.POST.get('reply')
        obj = Complaint.objects.get(complaint_id=idd)
        obj.reply = reply 
        obj.save()
    return render(request, 'complaints/subseller_post_reply.html')

def subseller_view_complaints(request):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid)
    print("======",owner_id.user_id)
    complaints = Complaint.objects.filter(owner_id=owner_id.user_id,reply='pending',product_type='old')
    context = {
        'complaints':complaints
    }
    return render(request, 'complaints/subseller_view_complaints.html',context)

def seller_view_complaints(request):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid)
    print("======",owner_id.user_id)
    complaints = Complaint.objects.filter(owner_id=owner_id.user_id,reply='pending',product_type='new')
    context = {
        'complaints':complaints
    }
    return render(request, 'complaints/seller_view_complaints.html',context)
